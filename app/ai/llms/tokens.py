
from .openai import calculate_openai_tokens

def calculate_tokens(texts):
    """
    Calculate tokens in a text
    """
    return calculate_openai_tokens(texts)