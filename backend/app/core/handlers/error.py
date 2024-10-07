from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR


class ErrorHandler:
    """
    A class to handle various types of errors in the FastAPI application,
    including invalid file types, corrupted images, Groq API errors,
    and generic internal server errors.
    """

    @staticmethod
    def handle_invalid_file_type():
        """
        Handle errors when the uploaded file is not a valid image type.

        Raises:
        HTTPException: If the uploaded file is not an image with an accepted type (jpeg, png, gif).
        """
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Only images (jpeg, png, gif) are accepted.",
        )

    @staticmethod
    def handle_invalid_image():
        """
        Handle errors when the uploaded image is corrupted or unreadable.

        Raises:
        HTTPException: If the uploaded image cannot be processed or is invalid.
        """
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="The uploaded file is not a valid image.",
        )

    @staticmethod
    def handle_groq_error(error_message: str):
        """
        Handle errors during the Groq API analysis process.

        Parameters:
        error_message (str): A message describing the error encountered during the Groq API analysis.

        Raises:
        HTTPException: If an error occurs during the interaction with the Groq API.
        """
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during Groq image analysis: {error_message}",
        )

    @staticmethod
    def handle_generic_error():
        """
        Handle generic internal server errors.

        Raises:
        HTTPException: If an unspecified internal error occurs.
        """
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal error occurred. Please try again later.",
        )
