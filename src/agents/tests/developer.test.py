import os
import asyncio

from prompts.developer import DEVELOPER_PROMPT


async def main():
    with open("amazon.txt", "r") as f:
        doc = f.read()

    developer_agent = DeveloperAgent(llm=client, requirements_doc=doc)
    await developer_agent.run()


if __name__ == "__main__":
    from models.llm.providers.openai import LLM_OpenAI
    from agents.developer import DeveloperAgent

    from dotenv import load_dotenv

    load_dotenv()

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

    client = LLM_OpenAI(api_key=OPENAI_API_KEY, sys_prompt=DEVELOPER_PROMPT)

    asyncio.run(main())
