"""
Enums
"""
from enum import Enum

# Define Enum for model names


class ModelNames(Enum):
    """
    Model names class
    """
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    GPT_4 = "gpt-4"
    GPT_4_TURBO_PREVIEW = "gpt-4-turbo-preview"
    GPT_4_MINI = "gpt-4o-mini"
    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"
    TEXT_EMBEDDING_3_LARGE = "text-embedding-3-large"
    TEXT_EMBEDDING_ADA_002 = "text-embedding-ada-002"


# Define the models dictionary using the Enum keys
MODELS = {
    ModelNames.GPT_3_5_TURBO: {
        "type": "chat",
        "input_cost": 0.0005,
        "output_cost": 0.0015
    },
    ModelNames.GPT_3_5_TURBO_16K: {
        "type": "chat",
        "input_cost": 0.003,
        "output_cost": 0.004
    },
    ModelNames.GPT_4: {
        "type": "chat",
        "input_cost": 0.03,
        "output_cost": 0.06
    },
    ModelNames.GPT_4_MINI: {
        "type": "chat",
        "input_cost": 0.0003,
        "output_cost": 0.008
    },
    ModelNames.GPT_4_TURBO_PREVIEW: {
        "type": "chat",
        "input_cost": 0.01,
        "output_cost": 0.03
    },
    ModelNames.TEXT_EMBEDDING_3_SMALL: {
        "type": "embedding",
        "cost": 0.00002
    },
    ModelNames.TEXT_EMBEDDING_3_LARGE: {
        "type": "embedding",
        "cost": 0.00013
    },
    ModelNames.TEXT_EMBEDDING_ADA_002: {
        "type": "embedding",
        "cost": 0.00010
    }
}

MODEL_COSTS = {
    ModelNames.GPT_3_5_TURBO.value: {"input": 0.0015, "output": 0.002},
    ModelNames.GPT_3_5_TURBO_16K.value: {"input": 0.003, "output": 0.004},
    ModelNames.GPT_4.value: {"input": 0.03, "output": 0.06},
    ModelNames.GPT_4_TURBO_PREVIEW.value: {"input": 0.01, "output": 0.03},
    ModelNames.GPT_4_MINI.value: {"input": 0.008, "output": 0.0015},
    ModelNames.TEXT_EMBEDDING_3_SMALL.value: 0.00002,
    ModelNames.TEXT_EMBEDDING_3_LARGE.value: 0.00013,
    ModelNames.TEXT_EMBEDDING_ADA_002.value: 0.00010
}
