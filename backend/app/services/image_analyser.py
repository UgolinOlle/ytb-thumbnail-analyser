from app.core.clients.groq import GroqClient
from app.core.handlers.error import ErrorHandler


async def analyze_thumbnail(image: bytes) -> dict:
    """
    Analyze a YouTube thumbnail using the Groq API and return a dynamic score
    based on the analysis.

    Parameters:
    image (bytes): The image file to be analyzed in bytes format.

    Returns:
    dict: A dictionary containing the dynamic score and the comment
    returned by the Groq API.

    Raises:
    HTTPException: If any error occurs during the API analysis.
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
        ErrorHandler.handle_groq_error(str(e))


def calculate_dynamic_score(comment: str) -> int:
    """
    Generate a dynamic score based on the analysis of the comment
    returned by the Groq API.

    The score is adjusted based on the presence of positive and
    negative keywords in the comment.

    Parameters:
    comment (str): The comment returned by Groq's analysis of the thumbnail.

    Returns:
    int: A dynamic score between 1 and 10.
    """
    try:
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

    except Exception as e:
        ErrorHandler.handle_generic_error()
