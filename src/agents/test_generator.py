import subprocess

from typing import Optional

from agents.abstract import Agent
from models.llm.abstract import GenerateParams
from models.llm.providers.providers import LLM_PROVIDERS

from constants import TEST_APP_SRC_DIR
from utils.file import join_paths


class TestGeneratorAgent(Agent):
    def __init__(
        self, llm: LLM_PROVIDERS, requirements_doc: str, base_dir: Optional[str] = None
    ):
        self.llm = llm
        self.requirement_doc = requirements_doc
        self.base_dir = base_dir if base_dir else TEST_APP_SRC_DIR

    async def run(self) -> None:
        print("TesterGenerator : Generating test cases...")

        prompt = (
            f"Here is the technical requirement document :\n\n {self.requirement_doc}"
        )

        # Setting max_tokens to 2048 since test cases are generally verbose
        params = GenerateParams(prompt=prompt, model="gpt-4o", max_tokens=2048)
        response = await self.llm.generate(params)
        test_code = response.get("generated_text", "Error in test generation")

        test_path = join_paths([self.base_dir, "App.test.js"])

        with open(test_path, "w") as file:
            file.write(test_code)

        print(f"TesterGenerator : Tests saved to {test_path}")

        if self.validate_code():
            print("TesterGenerator : Test cases are valid JavaScript code")
            return "SUCCESS"

        print("TesterGenerator : Test cases are invalid JavaScript code")
        return "ERROR"

    def validate_code(self: str) -> bool:
        try:
            print("TesterGenerator : Validating generated test cases")
            process = subprocess.Popen(
                ["npm", "run", "lint"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.base_dir,
            )

            for line in process.stdout:
                print(line, end="")
            for line in process.stderr:
                print(line, end="")

            process.wait()

            status = process.returncode == 0
            if status:
                print("TesterGenerator : Generated test cases are valid")
            else:
                print("TesterGenerator : Error occurred while validating code : ", process.returncode)

            return status
        
        except Exception as e:
            print(f"TesterGenerator : Error occurred while validating code : {e}")
            return False
