from typing import Optional, List
from pydantic import BaseModel, Field


class GenerateParams(BaseModel):
    model: str = ""

    sys_prompt : Optional[str] = ""

    # prompt can be optional if using images
    prompt: Optional[str] = ""

    max_tokens: Optional[int] = Field(
        100, gt=0, description="Maximum number of tokens to generate."
    )

    temperature: Optional[float] = Field(
        0.7, ge=0, le=1, description="Sampling temperature between 0 and 1."
    )

    top_p: Optional[float] = Field(
        0.9,
        ge=0,
        le=1,
        description="Nucleus sampling (top-p) parameter between 0 and 1.",
    )

    images: Optional[List[str]] = Field(
        None, description="List of image file paths to be processed."
    )
