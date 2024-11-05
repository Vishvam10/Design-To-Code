import os
import asyncio
from typing import List

from agents.abstract import Agent
from agents.types import AGENT_RETURN_TYPE

from utils.file import join_paths
from constants import TEST_APP_COMPONENTS_DIR


class ValidatorAgent(Agent):
    def __init__(self, folder_path: str = None):
        self.folder_path = folder_path if folder_path else TEST_APP_COMPONENTS_DIR
        self.files = self._get_files()

    def _get_files(self) -> List[str]:
        try:
            files = []
            for dirpath, _, filenames in os.walk(TEST_APP_COMPONENTS_DIR):
                for f in filenames:
                    files.append(join_paths([dirpath, f]))
            return files
        except Exception as e:
            print("Error occurred while scanning files:", str(e))
            return []

    async def _validate_file(self, file_path: str) -> bool:
        name, ext = os.path.splitext(file_path)
        if ext == ".jsx" or ext == ".js":
            return await self._validate_js_or_jsx_code(file_path)
        elif ext == ".css":
            return await self._validate_css_code(file_path)
        return True

    async def _validate_css_code(self, file_path: str) -> bool:
        try:
            process = await asyncio.create_subprocess_exec(
                "npm",
                "run",
                "lint:css",
                file_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=self.folder_path,
            )
            stdout, stderr = await process.communicate()
            if process.returncode == 0:
                return True
            else:
                print(f"Stylelint errors for {file_path}:\n{stderr.decode()}")
                return False
        except Exception as e:
            print(f"Error while validating CSS code for {file_path}: {e}")
            return False

    async def _validate_js_or_jsx_code(self, file_path: str) -> bool:
        try:
            process = await asyncio.create_subprocess_exec(
                "npm",
                "run",
                "lint:js",
                file_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=self.folder_path,
            )
            stdout, stderr = await process.communicate()
            if process.returncode == 0:
                return True
            else:
                print(f"ESLint errors for {file_path}:\n{stderr.decode()}")
                return False
        except Exception as e:
            print(f"Error while validating JS(X) code for {file_path}: {e}")
            return False

    async def run(self) -> AGENT_RETURN_TYPE:
        try:
            print()
            tasks = [self._validate_file(file_path) for file_path in self.files]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for file_path, result in zip(self.files, results):
                if isinstance(result, Exception):
                    print(f"Validator : Error processing file {file_path}: {result}")
                    return "ERROR"
                elif not result:
                    print(f"Validator : Validation failed for file: {file_path}")
                    return "FAILURE"
                else:
                    name, _ = os.path.splitext(os.path.basename(file_path))
                    print(f"Validator : Validation passed for file: {name}")

            print("\nValidator : Validation passed for all files\n")
            return "SUCCESS"

        except Exception as e:
            print("Error occurred while validating files:", str(e))
            return "ERROR"
