from typing import Union, Type

from models.llm.providers.groq import LLM_Groq
from models.llm.providers.openai import LLM_OpenAI

LLM_PROVIDERS = Type[Union[LLM_Groq, LLM_OpenAI]]
