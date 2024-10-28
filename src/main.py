import os
import asyncio

from models.llm.pydantic_models import GenerateParams
from models.segmentation.bounding_box import add_bounding_box

from prompts.system import SYSTEM_PROMPT
from prompts.test_generator import TEST_GENERATOR_PROMPT

from utils.file import join_paths, create_folder_structure
from constants import TESTS_DIR

INPUT_FOLDER = join_paths([TESTS_DIR, "layout", "input"])
OUTPUT_FOLDER = join_paths([TESTS_DIR, "layout", "output"])

IMAGE_NAME = "amazon"
IMAGE_PATH = f"{INPUT_FOLDER}/{IMAGE_NAME}.png"
ENHANCED_IAMGE_PATH = f"{INPUT_FOLDER}/{IMAGE_NAME}-enhanced.png"

LLM_MODEL = "gpt-4o"

OUTPUT_SAVE_FOLDER = join_paths([OUTPUT_FOLDER, LLM_MODEL])
create_folder_structure(OUTPUT_SAVE_FOLDER)


async def main():
    add_bounding_box([IMAGE_PATH], ENHANCED_IAMGE_PATH)

    prompt = "Given this design, generate a requirement doc for a frontend developer. Be as accurate and comprehensive as possible. We will be using this for production"

    image_paths = [IMAGE_PATH, ENHANCED_IAMGE_PATH]

    params = GenerateParams(
        model=LLM_MODEL, prompt=prompt, max_tokens=1024, images=image_paths
    )

    response = await client.generate(params)

    if "generated_text" in response:
        generated_text = response["generated_text"]

        print(IMAGE_NAME, "\n", generated_text)

        save_fp = join_paths([OUTPUT_SAVE_FOLDER, f"{IMAGE_NAME}.txt"])

        with open(save_fp, "w") as f:
            f.write(generated_text)
    else:
        print("Error in response :", response.get("error", "Unknown error occurred"))


if __name__ == "__main__":
    from models.llm.providers.openai import LLM_OpenAI
    from dotenv import load_dotenv

    load_dotenv()

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

    client = LLM_OpenAI(api_key=OPENAI_API_KEY, sys_prompt=SYSTEM_PROMPT)

    asyncio.run(main())
