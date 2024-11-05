import os
import asyncio

from prompts.test_generator import TEST_GENERATOR_PROMPT


async def main():
    
    test_generator = TestGeneratorAgent(llm=client)
    await test_generator.run(AvailableLLMs.OPENAI_GPT_4o)


if __name__ == "__main__":
    
    from models.llm.providers.openai import LLM_OpenAI
    from models.llm.providers.groq import LLM_Groq
    from models.llm.available_llms import AvailableLLMs

    from agents.test_generator import TestGeneratorAgent

    from dotenv import load_dotenv

    load_dotenv()

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

    with open("amazon.txt", "r") as f:
        doc = f.read()

    sys_prompt = TEST_GENERATOR_PROMPT.format(requirement_doc=doc)

    client = LLM_OpenAI(api_key=OPENAI_API_KEY, sys_prompt=sys_prompt)
    # client = LLM_Groq(api_key=GROQ_API_KEY, sys_prompt=sys_prompt)

    asyncio.run(main())
