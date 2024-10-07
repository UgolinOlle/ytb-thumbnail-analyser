from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from app.core.handlers.error_database import DatabaseErrorHandler
from .globals import settings


class Database:
    """
    Manages the database connection using SQLAlchemy and provides methods to connect,
    disconnect, and handle database sessions in a FastAPI application.
    """

    def __init__(self, database_url: str):
        """
        Initialize the Database class with the provided database URL.

        Parameters:
        database_url (str): The URL for connecting to the database.
        """
        self.database_url = database_url
        self.engine: Engine = None
        self.SessionLocal = None
        self.Base = declarative_base()

    def connect(self):
        """
        Establish the connection to the database by creating the SQLAlchemy engine
        and initializing the session factory.

        Raises:
        HTTPException: If the database connection fails, handled by DatabaseErrorHandler.
        """
        try:
            self.engine = create_engine(self.database_url, pool_pre_ping=True)
            self.SessionLocal = sessionmaker(
                autocommit=False, autoflush=False, bind=self.engine
            )
            print("Database connected.")
        except SQLAlchemyError as e:
            DatabaseErrorHandler.handle_connection_error(e)

    def disconnect(self):
        """
        Close the connection to the database by disposing of the SQLAlchemy engine.

        Raises:
        HTTPException: If the disconnection fails, handled by DatabaseErrorHandler.
        """
        try:
            if self.engine:
                self.engine.dispose()
                print("Database disconnected.")
        except SQLAlchemyError as e:
            DatabaseErrorHandler.handle_disconnection_error(e)

    def get_db(self):
        """
        Provide a database session for use in FastAPI routes.

        Yields:
        Session: A new SQLAlchemy session.

        Raises:
        HTTPException: If the session encounters an error, handled by DatabaseErrorHandler.
        """
        db = self.SessionLocal()
        try:
            yield db
        except SQLAlchemyError as e:
            DatabaseErrorHandler.handle_session_error(e)
        finally:
            try:
                db.close()
            except SQLAlchemyError as e:
                DatabaseErrorHandler.handle_session_closing_error(e)


db = Database(settings.DATABASE_URL)
