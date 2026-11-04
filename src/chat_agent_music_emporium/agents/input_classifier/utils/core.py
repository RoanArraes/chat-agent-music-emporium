from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

from chat_agent_music_emporium.agents.input_classifier.utils.prompts import (
    system_prompt_agent,
)
from chat_agent_music_emporium.agents.input_classifier.utils.state import (
    Answer,
)
from chat_agent_music_emporium.utils.settings import settings


def agent_core():
    model_classifier = 'gemini-3.5-flash-lite'

    model = ChatGoogleGenerativeAI(
        model=model_classifier,
        google_api_key=settings.GEMINI_API_KEY,
        max_retries=2,
    )

    system_prompt = system_prompt_agent

    return {
        'model': model,
        'system_prompt': system_prompt,
    }
