from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Engine
from .globals import settings


class Database:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine: Engine = None
        self.SessionLocal = None
        self.Base = declarative_base()

    def connect(self):
        """Creates the SQLAlchemy engine and sessionmaker."""
        self.engine = create_engine(self.database_url, pool_pre_ping=True)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        print("Database connected.")

    def disconnect(self):
        """Disposes the SQLAlchemy engine."""
        if self.engine:
            self.engine.dispose()
            print("Database disconnected.")

    def get_db(self):
        """Dependency for getting a session in FastAPI routes."""
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


db = Database(settings.DATABASE_URL)
