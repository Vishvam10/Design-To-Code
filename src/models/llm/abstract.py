from typing import Dict
from abc import ABC, abstractmethod

from models.llm.pydantic_models import GenerateParams

class LLM(ABC):
    @abstractmethod
    def generate(self, params: GenerateParams) -> Dict: ...
