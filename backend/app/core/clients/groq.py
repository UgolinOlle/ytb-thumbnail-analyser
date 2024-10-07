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
                                Analyze this YouTube thumbnail for its visual quality. Provide a score between 1 and 10,
                                considering factors like visual appeal, clarity, and overall design. Include a brief
                                comment highlighting areas for improvement and suggestions to make it more eye-catching
                                and effective. Add the maximum of detail possible.
                                For positive feedback, you may use terms like: 'excellent,' 'engaging,' 'vibrant,' 'clear,' 'eye-catching,' 'professional,' 'high quality.'
                                For constructive feedback, you may use terms like: 'blurry,' 'unclear,' 'dull,' 'confusing,' 'unprofessional,' 'low quality,' 'messy,' or 'distracting.'
                                Return only comment, without any additional text (no markdown allow).
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
