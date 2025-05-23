"""
load config module
"""
import os

from dotenv import load_dotenv

load_dotenv()

PDF_DIRECTORY = 'docs'
METADATA_FILE = 'document_metadata.json'

class App:
    """
    Store app specific configurations
    """
    APP_NAME = "AIAssistantModule"
    EUREKA_URL = os.getenv('EUREKA_URL')
    PORT = 8080
    MODEL_TYPE = os.getenv('MODEL_TYPE') # openai, ollama

class AuthConfig:
    """
    Store authetication related configurations
    """
    url = os.getenv('KEYCLOAK_AUTH_URL')

class Db:
    """
    Store DB related configurations
    """
    schema = os.getenv('DB_SCHEMA')
    connUrl = os.getenv('DB_CONNECTION_URL')

class OpenaiConfig:
    """
    Store OpenAI specific configurations
    """
    MODEL_NAME = os.getenv('OPEN_AI_MODEL')
    EMBEDDING_MODEL = "text-embedding-ada-002"

class OllamaConfig:
    """
    Store OpenAI specific configurations
    """
    MODEL_NAME = os.getenv('OLLAMA_MODEL')

class DeepSeekConfig:
    """
    Store Deepseek specific configurations
    """
    MODEL_NAME = os.getenv('DEEP_SEEK_MODEL')

class ChromaConfig:
    """
    Store chroma DB specific configurations
    """
    dir = 'db'
