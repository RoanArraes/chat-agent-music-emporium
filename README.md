## Passos para rodar o projeto:
 - Baixar ou clonar o projeto
 - Ter python instalado
 - Baixar e instalar uv
 - Acessar via terminal a pasta do projeto: chat-agent-music-emporium
 - Criar amb. virtual: uv venv .venv
 - Ativar amb. virtual: source .venv/bin/activate
 - Instalar dependências: uv sync
 - Criar arquivo .env
 - Inserir GEMINI_API_KEY = inserir sua api key gratuita do Gemini
 - Rodar o projeto: uv run start

 
## Justificativa das decisões técnicas:
LangGraph: Escolhi utilizar este framework devido ao controle do fluxo, customização de funções, 
    facilidade para detectar/isolar/corrigir erros e modularização com os SubGraphs.

LangChain: Utilizei para a criação dos agentes por abstrair boa parte da lógica de criação do agente e ao mesmo
    tempo ser altamente customizável e compatível com o LangGraph.

Estratégia geral: Criar um chat que recebe a mensagem do usuário, identifica a intenção através de um agente classificador,     
    direcionando o fluxo para um agente responsável pela busca no sql (status de pedido, preço de um item específico) 
    ou para um agente responsável pela busca semântica via banco vetorial (RAG) (políticas da loja, recomendações de itens
    próximos ao inserido pelo usuário, etc). Após este passo retorna para o agente responsável por receber os dados e
    responder para o usuário.

-> Decidi utilizar vários agentes mais simples devido a melhor eficiência de um prompt menor, diminuindo o risco de alucinações.
-> O uso de mais agentes facilita a modularização, identificação de problemas e possibilidade de melhorias sem impactar outras
  partes funcionais.



## Limitações conhecidas:
Com mais tempo concluiria o desenvolvimento da minha idéia, atuaria em tratamento de erros e melhorias no
no código / eficiência do prompt.


## Uso de assistentes de código:
Resolvi não utilizar, no momento estou buscando solidificar minha base de conhecimento e sinto que o uso de assistentes
  de código me atrapalham um pouco na fixação de novos conhecimentos.

Utilizo chat com llms quando não encontro algo nas documentações ou preciso entender algum erro específico.
