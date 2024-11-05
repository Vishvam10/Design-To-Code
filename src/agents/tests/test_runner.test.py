import asyncio

from agents.test_runner import TestRunnerAgent


async def main():
    test_runner = TestRunnerAgent()
    test_runner.run()


if __name__ == "__main__":
    asyncio.run(main())
