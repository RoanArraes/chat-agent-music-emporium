from langchain_core.messages import AIMessage
from chat_agent_music_emporium.graph.utils.functions import treat_human_input
from chat_agent_music_emporium.graph.utils.state import GraphState
from chat_agent_music_emporium.utils.messages import RESPONSE_CHAT_GREETINGS


def send_greetings_answer_node(state: GraphState):
    return GraphState(messages=[AIMessage(content=RESPONSE_CHAT_GREETINGS)])
