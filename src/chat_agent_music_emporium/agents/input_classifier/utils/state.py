from typing import Annotated
from langchain_core.messages import AIMessage, HumanMessage
from pydantic import BaseModel, Field


class MusicalInstrumentClassification(BaseModel):
    product: Annotated[str, 'Type of musical instrument']
    price: Annotated[str, 'Price of musical instrument']
    name: Annotated[str, 'Name of musical instrument']
    category: Annotated[str, 'Category of musical instrument']
    description: Annotated[str, 'Description of musical instrument']
    specs: Annotated[str, 'Specifications about musical instrument']


class Answer(BaseModel):
    #    classification: (
    #        Annotated[
    #            list[MusicalInstrumentClassification],
    #            'List of instrument based in the user input text',
    #        ]
    #        | None
    #    ) = Field(default=None)

    #    collection_vector_db: Annotated[
    #        str,
    #        'Avaliable collection of vector database based in the user text input',
    #    ]
    type_requested_service: Annotated[str, 'user message intent']


class GraphState(BaseModel):
    human_input_message: HumanMessage
    output_classifier: AIMessage | None = Field(default=None)
