import os
import asyncio

from agents.developer import DeveloperAgent
from agents.refactor import RefactorAgent
from agents.validator import ValidatorAgent
from agents.test_generator import TestGeneratorAgent
from agents.test_runner import TestRunnerAgent


async def main():
    
    dev_status = await developer_agent.run(
        model=AvailableLLMs.OPENAI_GPT_4o, sys_prompt=DEVELOPER_AGENT_SYSTEM_PROMPT
    )

    val_status = await validator_agent.run()
        




if __name__ == "__main__":
    from models.llm.providers.openai import LLM_OpenAI
    from models.llm.providers.groq import LLM_Groq
    from models.llm.available_llms import AvailableLLMs

    from prompts.developer import DEVELOPER_AGENT_SYSTEM_PROMPT
    from prompts.test_generator import TEST_GENERATOR_SYSTEM_PROMPT

    from dotenv import load_dotenv

    load_dotenv()

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

    with open("amazon.txt", "r") as f:
        doc = f.read()

    # sys_prompt = TEST_GENERATOR_PROMPT.format(requirement_doc=doc)

    # client = LLM_Groq(api_key=GROQ_API_KEY, sys_prompt=sys_prompt)
    client = LLM_OpenAI(api_key=OPENAI_API_KEY)

    developer_agent = DeveloperAgent(llm=client, requirements_doc=doc)
    refactor_agent = RefactorAgent()
    validator_agent = ValidatorAgent()
    test_generator_agent = TestGeneratorAgent(llm=client)
    test_runner_agent = TestRunnerAgent()

    asyncio.run(main())
