from functools import lru_cache
from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

# set the root directory of the project
BASE_DIR = Path(__file__).resolve().parents[2]

#create a class to hold the settings
class Settings(BaseSettings):
    app_name: str = "Enterprises IT Support Agentic RAG"
    app_env: str = "development"
    openai_api_key: str=""
    tavily_api_key: str=""
    pinecone_api_key: str=""
    pinecone_index_name: str="fde-it-support-rag"
    pinecone_namespace: str="company-it-kb"
    openai_model: str="gpt-4o-mini"
    embedding_model: str="text-embedding-3-small"
    top_k: int=4
    max_retrievals: int=1
    admin_api_key: str="nikhil_@2006"
    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    upload_dir: str = str(BASE_DIR / "uploads")
    sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")


    model_config=SettingsConfigDict(env_file=str(BASE_DIR / ".env"), extra="ignore")

@lru_cache
def get_settings():
    return Settings()   