import asyncio

from agents.validator import ValidatorAgent

async def main():
    
    test_generator = ValidatorAgent()
    await test_generator.run()


if __name__ == "__main__":
    
    asyncio.run(main())
