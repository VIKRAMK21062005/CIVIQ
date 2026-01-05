# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "CIVIQ API"
    PROJECT_VERSION: str = "1.0.0"
    
    # We will use SQLite for now because it requires no installation.
    # Later, we can switch to PostgreSQL by changing this string.
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./civiq.db")
    
    # Secret key for JWT Token generation (keep this safe in production!)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey12345")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()