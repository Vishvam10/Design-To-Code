from typing import Union

from models.llm.providers.groq import LLM_Groq
from models.llm.providers.openai import LLM_OpenAI

LLM_PROVIDERS = Union[LLM_Groq, LLM_OpenAI]
