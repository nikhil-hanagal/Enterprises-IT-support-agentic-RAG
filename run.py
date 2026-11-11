# from app.core.config import get_settings

# settings = get_settings()

# print(f"app name: {settings.app_name}")
# print(f"app env: {settings.app_env}")


from app.services.ingestion import load_file,chunk_documents
from pathlib import Path
from app.rag.vectorestore import add_document

docs=load_file(Path("data/sample_kb/company_IT_handbook.md"))
chunks=chunk_documents(docs)

add_document(chunks)

