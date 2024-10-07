from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Manages application settings by loading environment variables using Pydantic's BaseSettings.

    Attributes:
    DATABASE_URL (str): The database connection URL, required for connecting to the application's database.
    GROQ_API_KEY (str): The API key required for accessing the Groq service.

    Config:
    env_file (str): Specifies the path to the '.env' file where environment variables are defined.
    """

    DATABASE_URL: str
    GROQ_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
