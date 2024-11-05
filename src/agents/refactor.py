import re
import json

from uuid import uuid4
from typing import List, Dict

from agents.abstract import Agent
from agents.types import AGENT_RETURN_TYPE

from agents.models import ComponentData, ComponentDataWithImports

from constants import TEST_APP_SRC_DIR, TEST_APP_COMPONENTS_DIR

from utils.file import join_paths, get_relative_path, create_folder_structure
from utils.patterns import Patterns
from utils.print import TAB_SEP

APP_JSON_FILE_PATH = join_paths([TEST_APP_SRC_DIR, "App.json"])
UPDATED_APP_JSON_FILE_PATH = join_paths([TEST_APP_SRC_DIR, "AppUpdated.json"])


def get_default_component_name() -> str:
    return f"comp-{uuid4().hex[:8]}"


RefactorAgentOutput = Dict[str, ComponentDataWithImports]


class RefactorAgent(Agent):
    # Currently useless, but we will need this intermediate data later
    # For example, while creating component-specific test suites (although,
    # I think this would then be a global state, we'll see)
    component_data: RefactorAgentOutput = {}

    def __init__(self, app_txt_path: str = None):
        self.app_txt_path = app_txt_path if app_txt_path else APP_JSON_FILE_PATH
        create_folder_structure(TEST_APP_COMPONENTS_DIR)

    def _process_section(self, section: ComponentData):
        component_defn = section["definition"]
        component_styles = section["styles"]

        if component_defn:
            component_defn = component_defn.strip()
            component_name_match = re.search(
                Patterns.REACT_COMPONENT_DEFINITION_PATTERN.value,
                component_defn,
            )
            component_name = get_default_component_name()
            if component_name_match:
                component_name = component_name_match.group(1).strip()
            else:
                print(
                    "\nUsing auto-generated name for component:\n\n",
                    component_defn,
                )

            component_styles = component_styles.strip() if component_styles else ""
            imports = self._generate_imports(component_name, component_defn)

            self.component_data[component_name] = {
                "definition": component_defn,
                "styles": component_styles,
                "imports": imports,
            }

        else:
            print(f"No component definition found in section : {section}")

    def _generate_imports(self, name: str, definition: str) -> str:
        imports = "import React from 'react';\n"

        used_components = re.findall(
            Patterns.REACT_COMPONENT_NAME_EXTRACT_PATTERN.value, definition
        )
        defined_components = set(
            name for name in definition.split() if name.isidentifier()
        )

        for component in set(used_components):
            if component != name and component not in defined_components:
                # App.jsx is in /src and other components are in /src/components
                # so handling the relative file path stuff here. And we also
                # drop the .jsx file extension since that's how imports are done
                # in a React app
                if name == "App":
                    imports += f"import {component} from './components/{component}/{component}';\n"
                else:
                    imports += (
                        f"import {component} from './../{component}/{component}';\n"
                    )

        imports += "\nimport './index.css';\n"

        return imports

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

    def run(self) -> AGENT_RETURN_TYPE:
        print()
        print("Refactor : Splitting components and styles present in App.txt")

        with open(self.app_txt_path, "r") as file:
            data: List[ComponentData] = json.load(file)

        for section in data:
            self._process_section(section)

        print("\nRefactor : Components found :\n")
        for i, k in enumerate(self.component_data.keys()):
            print(f"{TAB_SEP} {i} : {k}")

        print()
        print("Refactor : Splitting components into files")

        for name, data in self.component_data.items():
            component_file_name = f"{name}.jsx"
            component_styles_file_name = "index.css"

            component_defn = (
                f"{data['imports']}\n{data['definition']}\n\nexport default {name};"
            )
            component_styles = data["styles"]

            component_file_path = self._write(name, component_file_name, component_defn)

            component_styles_file_path = self._write(
                name, component_styles_file_name, component_styles
            )

            print(f"\n{TAB_SEP} Component name : {name}")

            if component_file_path != "ERROR":
                print(f"{TAB_SEP} Definition registered to {component_file_path}")

            if component_styles_file_path != "ERROR":
                print(f"{TAB_SEP} Styles registered to {component_styles_file_path}")

        try:
            with open(UPDATED_APP_JSON_FILE_PATH, "w") as f:
                json.dump(self.component_data, f)

            print("Refactor : Component data with imports written to file")
            print()

            return "SUCCESS"

        except Exception as e:
            print("Error occurred while writing JSON to file : ", str(e))
            return "FAILURE"
