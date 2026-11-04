from langchain.agents import create_agent
from langchain_core.messages import AIMessage

from chat_agent_music_emporium.agents.input_classifier.utils.core import (
    agent_core,
)
from chat_agent_music_emporium.agents.input_classifier.utils.state import (
    GraphState,
)


def classifier_human_message_node(state: GraphState):
    agent = create_agent(**agent_core())
    result = agent.invoke({'messages': state.human_input_message})
    return {'output_classifier': result['messages'][-1]}
