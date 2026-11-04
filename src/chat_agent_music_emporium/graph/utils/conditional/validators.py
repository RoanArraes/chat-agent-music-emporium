from chat_agent_music_emporium.graph.utils.functions.treat_human_input import (
    verify_human_greetings,
)
from chat_agent_music_emporium.graph.utils.state import GraphState


def verify_human_input_conditional(state: GraphState):
    """
    Verifica se é uma saudação, se for retorna mensagem inicial de boas vindas.
    """
    if state.messages and state.messages[-1]:
        message = state.messages[-1].content
        if verify_human_greetings(i_h_message=message):
            return 'send_greetings'
    return 'continue'
