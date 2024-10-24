import base64
import time
import json

from typing import Dict, Any

from groq import AsyncGroq

from models.llm.abstract import GenerateParams


# Groq vision models don't support a system prompt. So, I'm excluding that
# here. Although for other models, it is supported so I'll probably add
# that model based check later
def generate_prompt_template(system_prompt: str, prompt: str, encoded_images: Any):
    msg = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": system_prompt + "\n\nInput Prompt :\n\n" + prompt,
                },
            ],
        },
    ]

    if encoded_images:
        for image in encoded_images:
            msg[0]["content"].append(
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{image}"},
                },
            )

    return msg


# Groq interface is literally the same as OpenAI. We could have used the OpenAI
# client and change the base_url and api_key param but meh.


class LLM_Groq:
    def __init__(self, api_key: str, sys_prompt: str = ""):
        self.api_key = api_key
        self.sys_prompt = sys_prompt
        self.client = AsyncGroq(api_key=self.api_key)

    async def generate(self, params: GenerateParams) -> Dict:
        try:
            encoded_images = []
            encoding_time, api_response_time = 0, 0
            total_length = 0

            if params.images:
                for image in params.images:
                    start = time.time()

                    with open(image, "rb") as img_file:
                        image_data = img_file.read()

                    encoded_image = base64.b64encode(image_data).decode("utf-8")
                    encoded_images.append(encoded_image)
                    total_length += len(encoded_image)

                    print("Encoded image : ", len(encoded_image))

                    end = time.time()
                    encoding_time += end - start

            print("\nTotal length : ", total_length)

            input_data = generate_prompt_template(
                self.sys_prompt, params.prompt, encoded_images
            )

            api_params = {
                "model": params.model,
                "messages": input_data,
                "max_tokens": params.max_tokens,
                "temperature": params.temperature,
                "top_p": params.top_p,
            }

            start = time.time()

            response = await self.client.chat.completions.create(**api_params)
            generated_text = response.choices[0].message.content.strip()
            usage = response.usage

            end = time.time()

            api_response_time = end - start

            LOG_OBJ = {
                "input_tokens": usage.prompt_tokens,
                "output_tokens": usage.completion_tokens,
                "total_tokens": usage.total_tokens,
                "encoding_time": encoding_time,
                "api_response_time": api_response_time,
            }

            print("\n", json.dumps(LOG_OBJ, indent=2), "\n")
            with open("debug.log", "a") as json_file:
                json.dump(LOG_OBJ, json_file, indent=2)

            return {"generated_text": generated_text}

        except Exception as e:
            print(e)
            return {"error": "Error occurred while generating response"}
