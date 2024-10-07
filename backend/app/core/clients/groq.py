from groq import Groq
import base64

from app.core.configs.globals import settings


class GroqClient:
    _instance = None
    _api_key = settings.GROQ_API_KEY

    def __new__(cls):
        """
        Initialiser le client une seule fois et renvoyer la même instance.
        """
        if cls._instance is None:
            cls._instance = super(GroqClient, cls).__new__(cls)
            cls._instance.client = Groq(api_key=cls._api_key)
        return cls._instance

    def analyze_image(self, image_bytes: bytes) -> str:
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """
                                Ceci est une miniature YouTube. Analyse-la et évalue sa qualité sur une échelle de
                                1 à 10 en te basant uniquement sur l'attrait visuel et la clarté. Propose des suggestions
                                d\'amélioration pour rendre la miniature plus percutante. Donne-moi uniquement le
                                commentaire
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
