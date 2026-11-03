from langgraph.graph import StateGraph, START, END

from chat_agent_music_emporium.graph.utils.conditional.validators import (
    verify_human_input_conditional,
)
from chat_agent_music_emporium.graph.utils.nodes import (
    send_greetings_answer_node,
)
from chat_agent_music_emporium.graph.utils.state import GraphState


graph_builder = StateGraph(GraphState)

graph_builder.add_node(
    'verify_human_input_conditional', verify_human_input_conditional
)
graph_builder.add_node(
    'send_greetings_answer_node', send_greetings_answer_node
)

graph_builder.add_conditional_edges(
    START,
    verify_human_input_conditional,
    {'send_greetings': 'send_greetings_answer_node', 'continue': END},
)
graph_builder.add_edge('send_greetings_answer_node', END)

graph = graph_builder.compile()
