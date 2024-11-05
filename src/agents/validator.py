import subprocess

from typing import List, TypedDict

from agents.abstract import Agent
from agents.types import AGENT_RETURN_TYPE

from constants import TEST_APP_SRC_DIR
from utils.file import join_paths

APP_TXT_FILE_PATH = join_paths([TEST_APP_SRC_DIR, "App.txt"])


class FileMetadata(TypedDict):
    file_name: str
    file_path: str
    file_extension: str


ValidatorAgentInput = List[FileMetadata]

class ValidatorAgent(Agent):
    def __init__(self, file_data: ValidatorAgentInput):
        self.file_data = file_data

    async def run(self) -> AGENT_RETURN_TYPE:
        try:
            print()
            for data in self.file_data:
                name = data["file_name"]
                path = data["file_path"]
                ext = data["file_extension"]

                if ext == "jsx" or ext == "js":
                    is_valid = self._validate_js_or_jsx_code(path)

                elif ext == "css":
                    is_valid = self._validate_css_code(path)

                if not is_valid:
                    print(f"Validator : Validation failed for file : {path}")
                    return "FAILURE"

                print(f"Validator : Validation passed for file : {name} ")

            print("\nValidator : Validation passed for all files\n")
            return "SUCCESS"

        except Exception as e:
            print("Error occurred while generating React code : ", str(e))
            return "ERROR"

    def _validate_css_code(self, file_path: str) -> bool:
        try:
            result = subprocess.run(
                ["npx", "stylelint", file_path], capture_output=True, text=True
            )

            if result.returncode == 0:
                return True
            else:
                print("Stylelint errors : ")
                print(result.stderr)
                return False
        except Exception as e:
            print(f"Error while validating CSS code : {e}")
            return False

    def _validate_js_or_jsx_code(self, file_path: str) -> bool:
        try:
            result = subprocess.run(
                ["npx", "eslint", file_path], capture_output=True, text=True
            )

            if result.returncode == 0:
                return True
            else:
                print("ESLint errors : ")
                print(result.stderr)
                return False
        except Exception as e:
            print(f"Error while validating JS(X) code : {e}")
            return False
