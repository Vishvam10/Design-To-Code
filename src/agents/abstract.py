from typing import Any
from abc import ABC, abstractmethod


# NOTE : An agent CAN change the system prompt if an LLM is passed.
# If an agent does that, make sure to reset it at the end of run() method
class Agent(ABC):
    @abstractmethod
    def run(self) -> Any: ...
