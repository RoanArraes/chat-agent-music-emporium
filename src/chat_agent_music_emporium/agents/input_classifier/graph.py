from langgraph.graph import StateGraph, START, END

from chat_agent_music_emporium.agents.input_classifier.utils.nodes import (
    classifier_human_message_node,
)
from chat_agent_music_emporium.agents.input_classifier.utils.state import (
    GraphState,
)


agent_builder = StateGraph(GraphState)

agent_builder.add_node(
    'classifier_human_message_node', classifier_human_message_node
)

agent_builder.add_edge(START, 'classifier_human_message_node')

agent_input_classifier_graph = agent_builder.compile()
