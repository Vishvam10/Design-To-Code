import subprocess

from typing import Optional

from agents.abstract import Agent
from models.llm.providers.providers import LLM_PROVIDERS

from constants import TEST_APP_SRC_DIR


class TestRunnerAgent(Agent):
    def __init__(self, llm: LLM_PROVIDERS, test_dir: Optional[str] = None) -> None:
        self.llm = llm
        self.test_dir = test_dir if test_dir else TEST_APP_SRC_DIR

    def run(self: str) -> bool:
        try:
            print("TestRunner : Running generated test cases")
            process = subprocess.Popen(
                ["npm", "run", "test"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.test_dir,
            )

            for line in process.stdout:
                print(line, end="")
            for line in process.stderr:
                print(line, end="")

            process.wait()

            status = process.returncode == 0

            if status:
                print("TestRunner : Generated test cases are valid")
            else:
                print(
                    "TestRunner : Error occurred while validating code : ",
                    process.returncode,
                )

            return status

        except Exception as e:
            print(f"TestRunner : Error occurred while validating code : {e}")
            return False
