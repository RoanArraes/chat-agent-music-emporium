from langchain_core.messages import HumanMessage
from chat_agent_music_emporium.graph.graph import graph


human_input = str(input(''))
messages = [HumanMessage(content=human_input)]
result = graph.invoke({'messages': messages})

print(result['messages'][-1].content)
