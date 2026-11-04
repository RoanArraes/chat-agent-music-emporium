from langchain_core.messages import AIMessage
from chat_agent_music_emporium.agents.input_classifier.graph import (
    agent_input_classifier_graph,
)
from chat_agent_music_emporium.graph.utils.functions import treat_human_input
from chat_agent_music_emporium.graph.utils.state import GraphState
from chat_agent_music_emporium.utils.messages import RESPONSE_CHAT_GREETINGS


def send_greetings_answer_node(state: GraphState):
    return GraphState(
        messages=[AIMessage(content=[{'text': RESPONSE_CHAT_GREETINGS}])]
    )


def call_agent_input_classifier_node(state: GraphState):
    subgraph_output = agent_input_classifier_graph.invoke({
        'human_input_message': state.messages[-1]
    })
    return {'messages': [subgraph_output['output_classifier']]}
