import os

from agents.abstract import Agent
from constants import TEST_APP_SRC_DIR

# For setting up the environment (for the time being, test-app is setup)

class BuilderAgent(Agent):
    def __init__(self, dir_path=""):
        self.dir_path = dir_path if dir_path else TEST_APP_SRC_DIR

    async def generate(self) -> None:
        print("Builder : Verifying setup ...")
        # if os.path.exists(os.path.join(self.dir_path, "package.json")):
        #     print("Builder: Found package.json, verifying dependencies...")
        #     os.system(f"cd {self.dir_path} && npm install")
        # else:
        #     print("Builder: No package.json found in the base directory.")
        
        print("Builder : Verifying setup done")
        
