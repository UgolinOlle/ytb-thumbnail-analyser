from groq import Groq
import base64

from app.core.configs.globals import settings


class GroqClient:
    """
    Singleton class to handle interactions with the Groq API for analyzing YouTube thumbnails.
    This class ensures that only one instance of the Groq client is created during the lifetime
    of the application.
    """

    _instance = None
    _api_key = settings.GROQ_API_KEY

    def __new__(cls):
        """
        Initialize the Groq client once and return the same instance for future requests.

        Returns:
        GroqClient: A single instance of the GroqClient.
        """
        if cls._instance is None:
            cls._instance = super(GroqClient, cls).__new__(cls)
            cls._instance.client = Groq(api_key=cls._api_key)
        return cls._instance

    def analyze_image(self, image_bytes: bytes) -> str:
        """
        Analyze a YouTube thumbnail using the Groq API and return the generated comment.

        Parameters:
        image_bytes (bytes): The image data to be analyzed, in bytes format.

        Returns:
        str: A comment suggesting how the thumbnail could be improved based on its visual quality and clarity.
        """
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """
                                This is a YouTube thumbnail. Please analyze its visual quality and rate it on a scale
                                of 1 to 10, based on its visual appeal, clarity, and design. Provide constructive
                                feedback on how the thumbnail can be improved to make it more eye-catching and
                                effective.

                                For positive feedback, consider using terms like:
                                "excellent", "clear", "engaging", "vibrant", "well-designed", "eye-catching",
                                "professional", "impactful", "compelling", "high quality".

                                For negative feedback, consider using terms like:
                                "poor", "blurry", "unclear", "boring", "unprofessional", "confusing",
                                "messy", "low quality", "distracting", "incomplete".

                                Only return the comment and NOTHING else.
                            """,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model="llama-3.2-11b-vision-preview",
        )

        comment = chat_completion.choices[0].message.content
        return comment
