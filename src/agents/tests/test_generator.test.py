import os
import asyncio

from prompts.test_generator import TEST_GENERATOR_PROMPT


async def main():
    with open("amazon.txt", "r") as f:
        doc = f.read()

    test_generator = TestGeneratorAgent(llm=client, requirements_doc=doc)
    await test_generator.generate()


if __name__ == "__main__":
    from models.llm.providers.openai import LLM_OpenAI
    from agents.test_generator import TestGeneratorAgent

    from dotenv import load_dotenv

    load_dotenv()

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

    client = LLM_OpenAI(api_key=OPENAI_API_KEY, sys_prompt=TEST_GENERATOR_PROMPT)

    asyncio.run(main())