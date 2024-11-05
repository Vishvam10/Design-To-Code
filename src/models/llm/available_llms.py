from enum import Enum

class AvailableLLMs(Enum):
    
    # Groq
    GROQ_GEMMA_7B_IT = "gemma-7b-it"
    GROQ_LLAMA_3_1_8B_INSTANT = "llama-3.1-8b-instant"
    GROQ_WHISPER_LARGE_V3 = "whisper-large-v3"
    GROQ_LLAMA3_GROQ_8B_8192_TOOL_USE_PREVIEW = "llama3-groq-8b-8192-tool-use-preview"
    GROQ_LLAMA3_8B_8192 = "llama3-8b-8192"
    GROQ_LLAVA_V1_5_7B_4096_PREVIEW = "llava-v1.5-7b-4096-preview"
    GROQ_LLAMA_GUARD_3_8B = "llama-guard-3-8b"
    GROQ_LLAMA_3_1_70B_VERSATILE = "llama-3.1-70b-versatile"
    GROQ_LLAMA_3_2_11B_TEXT_PREVIEW = "llama-3.2-11b-text-preview"
    GROQ_LLAMA3_GROQ_70B_8192_TOOL_USE_PREVIEW = "llama3-groq-70b-8192-tool-use-preview"
    GROQ_LLAMA_3_2_11B_VISION_PREVIEW = "llama-3.2-11b-vision-preview"
    GROQ_GEMMA2_9B_IT = "gemma2-9b-it"
    GROQ_DISTIL_WHISPER_LARGE_V3_EN = "distil-whisper-large-v3-en"
    GROQ_WHISPER_LARGE_V3_TURBO = "whisper-large-v3-turbo"
    GROQ_LLAMA_3_2_1B_PREVIEW = "llama-3.2-1b-preview"
    GROQ_LLAMA_3_2_3B_PREVIEW = "llama-3.2-3b-preview"
    GROQ_LLAMA3_70B_8192 = "llama3-70b-8192"
    GROQ_MIXTRAL_8X7B_32768 = "mixtral-8x7b-32768"
    GROQ_LLAMA_3_2_90B_TEXT_PREVIEW = "llama-3.2-90b-text-preview"
    GROQ_LLAMA_3_2_90B_VISION_PREVIEW = "llama-3.2-90b-vision-preview"

    # OpenAI
    OPENAI_GPT_4o = "gpt-4o"