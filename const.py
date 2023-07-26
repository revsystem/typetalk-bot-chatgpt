import openai
import os

# Typetalk API URL
# https://developer.nulab.com/docs/typetalk/auth/
TYPETALK_API_URL = "https://typetalk.com/api/v1"

# Typetalk Topic parameters
TYPETALK_TOPIC_ID = os.environ["TYPETALK_TOPIC_ID"]
TYPETALK_API_ENDPOINT = f"{TYPETALK_API_URL}/topics/{TYPETALK_TOPIC_ID}"
TYPETALK_TOKEN = os.environ["TYPETALK_TOKEN"]

# Typetalk API parameters
TYPETALK_TALK_COUNT = 8
TYPETALK_TAKL_DIRECTION = "backward"

# OpenAI API parameters
openai.api_key = os.environ["OPENAI_API_KEY"]

# ChatGPT Request Body parameters
# https://platform.openai.com/docs/api-reference/completions/create
OPENAI_MODEL = "gpt-4"
OPENAI_TEMPERATURE = 0.85
OPENAI_MAX_TOKENS = 1024
OPENAI_TOP_P = 1.0
OPENAI_FREQUENCY_PENALTY = 0
OPENAI_PRESENCE_PENALTY = 0

# ChatGPT character
CHARACTER = f"You are a technical writer with expertise in online communications; please respond to the following requirements.\
- Use a calm tone of voice in your conversation.\
- Avoid vague answers.  \
- Please avoid technical jargon whenever possible and limit your response to 200 to 300 words."
