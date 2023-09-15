import os
from dotenv import load_dotenv

load_dotenv()

# App
FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")

# Database
#MONGODB_URI = (
#    os.getenv("MONGODB_URI_DEV")
#    if FLASK_ENV == "development"
#    else os.getenv("MONGODB_URI_PROD")
#)

# Secrets
SECRET_KEY = os.getenv("SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WHATSAPP_LOCAL_TOKEN = os.getenv("WHATSAPP_LOCAL_TOKEN")
WHATSAPP_BEARER_TOKEN = os.getenv("WHATSAPP_BEARER_TOKEN")

# APIs
WHATSAPP_API_URL: str = ""

# Prompts
INITIAL_PROMPT: str = "Você é um especialista em finanças pessoais. Eu não tenho conhecimento em finanças."
MESSAGES_LIMIT: int = 10
ANSWER_SENTENCE_LIMIT: int = 2
