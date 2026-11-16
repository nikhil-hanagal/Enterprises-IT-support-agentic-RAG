
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    # Application settings
    app_name: str = "Enterprises IT Support Agentic RAG"
    app_env: str = "development"

    # Groq LLM configuration
    groq_api_key: str = ""
    groq_model: str = "openai/gpt-oss-20b"

    # Existing Hugging Face embedding configuration
    huggingFace_model: str = "sentence-transformers/all-mpnet-base-v2"
    embedding_model: str = "sentence-transformers/all-mpnet-base-v2"

    # Tavily configuration
    tavily_api_key: str = ""

    # Pinecone configuration
    pinecone_api_key: str = ""
    pinecone_index_name: str = "fde-it-support-rag"
    pinecone_namespace: str = "company-it-kb-hf"

    # Retrieval configuration
    top_k: int = 4
    max_retrievals: int = 1

    # Application paths
    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    upload_dir: str = str(BASE_DIR / "uploads")
    sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")

    # Admin configuration
    admin_api_key: str = "nikhil@2006"

    # Environment configuration
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()
