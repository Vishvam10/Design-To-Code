import os

from agents.refactor import RefactorAgent

from constants import SRC_DIR
from utils.file import join_paths

APP_TXT_PATH = join_paths([SRC_DIR, "agents", "tests", "app.txt"])

def main():

    refactor_agent = RefactorAgent(app_txt_path=APP_TXT_PATH)
    refactor_agent.run()


if __name__ == "__main__":
    
    main()