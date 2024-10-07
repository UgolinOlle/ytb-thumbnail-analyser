from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR


class ErrorHandler:
    @staticmethod
    def handle_invalid_file_type():
        """
        Handle errors when the uploaded file is not a valid image type.
        """
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Only images (jpeg, png, gif) are accepted.",
        )

    @staticmethod
    def handle_invalid_image():
        """
        Handle errors when the uploaded image is corrupted or unreadable.
        """
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="The uploaded file is not a valid image.",
        )

    @staticmethod
    def handle_groq_error(error_message: str):
        """
        Handle errors during the Groq API analysis process.
        """
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during Groq image analysis: {error_message}",
        )

    @staticmethod
    def handle_generic_error():
        """
        Handle generic internal server errors.
        """
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal error occurred. Please try again later.",
        )
