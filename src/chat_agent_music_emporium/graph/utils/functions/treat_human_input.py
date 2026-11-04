import re

from chat_agent_music_emporium.utils.messages import RESPONSE_CHAT_GREETINGS


def verify_human_greetings(i_h_message: str):
    """
    Analisa a mensagem do usuário. Se existir uma saudação retorna True,
    caso contrário retorna False
    """

    greetings_pattern = re.compile(
        r'^(oi+a*|ola?|bom\s+dia|boa\s+tarde|boa\s+noite|hey+|hello|hi|opa|tudo\s+b+e+m\??)\b',
        re.IGNORECASE,
    )

    cleared_text = i_h_message.strip()
    text_without_accents = re.sub(r'[!?.,]', '', cleared_text)

    if (
        greetings_pattern.findall(text_without_accents.lower())
        or not i_h_message
    ):
        return True

    return False
