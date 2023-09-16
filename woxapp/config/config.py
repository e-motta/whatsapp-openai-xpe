import os
from dotenv import load_dotenv

load_dotenv()

# App
FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")

# Database

MONGODB_URI = os.getenv("MONGODB_URI")
#    if FLASK_ENV == "development"
#    else os.getenv("MONGODB_URI_PROD")
# )

# Secrets
SECRET_KEY = os.getenv("SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WHATSAPP_LOCAL_TOKEN = os.getenv("WHATSAPP_LOCAL_TOKEN")
WHATSAPP_BEARER_TOKEN = os.getenv("WHATSAPP_BEARER_TOKEN")

# APIs
WHATSAPP_API_URL: str = os.getenv("WHATSAPP_API_URL")

# Prompts
INITIAL_PROMPT: str = """
Você é um especialista em finanças pessoais.
Você adota uma postura pedagógica e esclarecedora, guiando-me
com perguntas sempre que necessário.
Eu não tenho conhecimento em finanças.
Você procura responder as perguntas de forma objetiva e direta, 
procurando utilizar, no máximo, três a quatro frases para as respostas.
Se eu fizer questões que não forem relativas à finanças, você deve responder que 
não pode ajudar com outros assuntos, pois é apenas um consultor para finanças pessoais.
"""
MESSAGES_LIMIT: int = 10
ANSWER_SENTENCE_LIMIT: int = 2
