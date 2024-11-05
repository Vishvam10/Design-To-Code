import subprocess
from typing import Optional

from agents.abstract import Agent
from agents.types import AGENT_RETURN_TYPE

from constants import TEST_APP_SRC_DIR


class TestRunnerAgent(Agent):
    def __init__(self, test_dir: Optional[str] = None) -> None:
        self.test_dir = test_dir if test_dir else TEST_APP_SRC_DIR

    def run(self) -> AGENT_RETURN_TYPE:
        try:
            print("TestRunner : Running generated test cases")
            process = subprocess.Popen(
                ["npm", "run", "test"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.test_dir,
            )

            # Communicate with the process to get stdout and stderr
            stdout, stderr = process.communicate()

            if stdout:
                print(stdout.strip())
            if stderr:
                print(stderr.strip())

            return_code = process.returncode

            if return_code == 0:
                print("TestRunner : All test cases passed")
                return "SUCCESS"
            else:
                # We assume that a non-zero return code from the tests 
                # themselves (e.g., test failures) is acceptable; only report 
                # as an error if the command itself failed (like script not 
                # found).
                if return_code > 1:
                    print(
                        "TestRunner : Error occurred while running tests:",
                        return_code,
                    )
                    return "ERROR"
                else:
                    print("TestRunner : Test cases failed")
                    return "FAILURE"

        except Exception as e:
            print(f"TestRunner : Error occurred while validating code: {e}")
            return "ERROR"
