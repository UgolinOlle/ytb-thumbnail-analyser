from app.core.clients.groq import GroqClient
from fastapi import HTTPException


async def analyze_thumbnail(image: bytes) -> dict:
    """
    Utilise le client Groq pour analyser la miniature et retourne un score dynamique.
    """
    try:
        client = GroqClient()
        result = client.analyze_image(image)
        score = calculate_dynamic_score(result)

        return {
            "score": score,
            "comment": result,
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de l'analyse de la miniature: {str(e)}",
        )


def calculate_dynamic_score(comment: str) -> int:
    """
    Génère un score dynamique basé sur l'analyse du commentaire retourné.
    """
    positive_keywords = ["excellent", "bien", "clair", "attrayant", "parfait"]
    negative_keywords = ["mauvais", "flou", "incomplet", "difficile", "problème"]
    score = 5

    for word in positive_keywords:
        if word in comment.lower():
            score += 1

    for word in negative_keywords:
        if word in comment.lower():
            score -= 1

    return max(1, min(10, score))
