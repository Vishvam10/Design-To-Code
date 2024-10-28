from typing import Any
from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def run(self) -> Any : ...