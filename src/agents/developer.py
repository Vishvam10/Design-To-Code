from agents.abstract import Agent
from agents.types import AGENT_RETURN_TYPE

from models.llm.abstract import GenerateParams
from models.llm.providers.providers import LLM_PROVIDERS

from constants import TEST_APP_SRC_DIR
from utils.file import join_paths

APP_JSON_FILE_PATH = join_paths([TEST_APP_SRC_DIR, "App.json"])


class DeveloperAgent(Agent):
    def __init__(self, llm: LLM_PROVIDERS, requirements_doc: str, save_fp: str = None):
        self.llm = llm
        self.requirements_doc = requirements_doc
        self.save_fp = save_fp if save_fp else APP_JSON_FILE_PATH

    async def run(
        self, model: str = "gpt-4o", sys_prompt: str = ""
    ) -> AGENT_RETURN_TYPE:
        try:
            print("Developer : Generating React code ...")
            params = GenerateParams(
                model=model,
                sys_prompt=sys_prompt,
                prompt=self.requirements_doc,
                max_tokens=2048,
            )
            response = await self.llm.generate(params)
            react_code = response.get("generated_text", "Error in code generation")

            with open(self.save_fp, "w") as file:
                file.write(react_code)

            print(f"Developer : Code saved to {self.save_fp}")

            return react_code

        except Exception as e:
            print("Error occurred while generating React code : ", str(e))
            return "ERROR"
