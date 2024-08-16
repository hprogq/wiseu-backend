import os

class ChromaDBConfig:
    CHROMADB_HOST = os.getenv("CHROMADB_HOST", "localhost")
    CHROMADB_PORT = int(os.getenv("CHROMADB_PORT", 9000))
    CHROMADB_COLLECTION = os.getenv("CHROMADB_COLLECTION", "your_collection_name")
