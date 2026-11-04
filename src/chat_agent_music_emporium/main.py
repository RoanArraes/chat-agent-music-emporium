from langchain_core.messages import HumanMessage
from chat_agent_music_emporium.graph.graph import graph


def start():
    human_input = str(input('Pergunta: '))
    messages = [HumanMessage(content=human_input)]
    result = graph.invoke({'messages': messages})

    print(f'Resposta IA: {result["messages"][-1].content[0]["text"]}')


if __name__ == '__main__':
    start()
