import asyncio
import json

from typing import Dict

from agents.abstract import Agent
from agents.types import AGENT_RETURN_TYPE
from agents.models import ComponentDataWithImports

from models.llm.abstract import GenerateParams
from models.llm.providers.providers import LLM_PROVIDERS

from constants import TEST_APP_SRC_DIR, TEST_APP_COMPONENTS_DIR
from utils.file import join_paths, get_relative_path, create_folder_structure

UPDATED_APP_JSON_FILE_PATH = join_paths([TEST_APP_SRC_DIR, "AppUpdated.json"])

TestGeneratorAgentInput = Dict[str, ComponentDataWithImports]

# This was a breaking change in version 6.0 that removed the extend-expect
# entry point in favor of a default entry point and some platform specific
# ones. For my use case, the default entry point worked:
IMPORTS_TO_REMOVE = ["import '@testing-library/jest-dom/extend-expect';"]


class TestGeneratorAgent(Agent):
    def __init__(self, llm: LLM_PROVIDERS):
        self.llm = llm
        self.component_data: TestGeneratorAgentInput = self._get_component_data()

    def _get_component_data(self):
        with open(UPDATED_APP_JSON_FILE_PATH, "r") as f:
            data = json.load(f)

        return data

    async def _generate_test_suite(self, name, data, model, llm):
        print(f"TesterGenerator : Generating test suite for {name}")

        react_code = (
            f"{data['imports']}\n{data['definition']}\n\nexport default {name};"
        )

        style = data["styles"]

        prompt = (
            f"\n\nHere's the React code for component {name} : \n\n{react_code}. "
            f"\n\nHere's are the component's CSS styles : \n\n{style}"
        )

        # Setting max_tokens to 4096 since test cases are generally verbose
        params = GenerateParams(prompt=prompt, model=model, max_tokens=4096)

        response = await llm.generate(params)

        if response is None:
            print(f"No response received from the model for {name}.")
            return None

        test_suite = response.get("generated_text", "Error in code generation")

        for item in IMPORTS_TO_REMOVE:
            test_suite.replace(item, "")

        component_file_name = f"{name}.spec.js"

        component_test_file_path = self._write(name, component_file_name, test_suite)
        print(
            f"TesterGenerator : Test suite for {name} saved to {component_test_file_path}"
        )

        return component_test_file_path

    def _write(self, component_name: str, file_name: str, data: str) -> str:
        try:
            if not component_name.startswith("App"):
                component_folder_path = join_paths(
                    [TEST_APP_COMPONENTS_DIR, component_name]
                )
                create_folder_structure(component_folder_path)
                file_path = join_paths([component_folder_path, file_name])
            else:
                # We want the App.jsx file to be present in /src not
                # in /src/components
                file_path = join_paths([TEST_APP_SRC_DIR, file_name])

            # It is easier to read on the terminal
            relative_file_path = get_relative_path(file_path, TEST_APP_SRC_DIR)

            # print("\nWriting stuff to : ", file_path)
            # print("\n\nStuff : \n\n", data)

            with open(file_path, "w") as f:
                f.write(data)

            return relative_file_path

        except Exception as e:
            print(f"Error occurred while writing to file: {file_path}: ", e)
            return "ERROR"

    async def run(self, model: str) -> AGENT_RETURN_TYPE:
        try:
            print()
            tasks = []
            for name, data in self.component_data.items():
                tasks.append(self._generate_test_suite(name, data, model, self.llm))

            await asyncio.gather(*tasks)

            return "SUCCESS"

        except Exception as e:
            print("Error occurred while generating test suites: ", str(e))
            return "ERROR"
