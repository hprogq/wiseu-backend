import os

class DatabaseConfig:
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_NAME = os.getenv("DB_NAME")
    DB_TABLE_PREFIX = os.getenv("DB_TABLE_PREFIX", "wiseu_")

    @classmethod
    def get_connection_string(cls):
        return f"postgresql://{cls.DB_USERNAME}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
