from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR


class DatabaseErrorHandler:
    """
    Handles errors related to database connections, sessions, and disconnections.
    This class centralizes error handling for the Database class.
    """

    @staticmethod
    def handle_connection_error(error: SQLAlchemyError):
        """
        Handle database connection errors.

        Parameters:
        error (SQLAlchemyError): The exception raised during the connection attempt.

        Raises:
        HTTPException: If the database connection fails.
        """
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed: {str(error)}",
        )

    @staticmethod
    def handle_disconnection_error(error: SQLAlchemyError):
        """
        Handle database disconnection errors.

        Parameters:
        error (SQLAlchemyError): The exception raised during the disconnection attempt.

        Raises:
        HTTPException: If the database disconnection fails.
        """
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database disconnection failed: {str(error)}",
        )

    @staticmethod
    def handle_session_error(error: SQLAlchemyError):
        """
        Handle errors when creating or closing a database session.

        Parameters:
        error (SQLAlchemyError): The exception raised during session management.

        Raises:
        HTTPException: If the database session encounters an error.
        """
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database session error: {str(error)}",
        )

    @staticmethod
    def handle_session_closing_error(error: SQLAlchemyError):
        """
        Handle errors when closing a session.

        Parameters:
        error (SQLAlchemyError): The exception raised during the session close attempt.

        Raises:
        HTTPException: If the database session fails to close properly.
        """
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error closing the database session: {str(error)}",
        )
