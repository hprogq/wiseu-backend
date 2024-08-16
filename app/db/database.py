from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DatabaseConfig

engine = create_engine(DatabaseConfig.get_connection_string())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
