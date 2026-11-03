import operator
from typing import Annotated

from langchain_core.messages import AnyMessage
from pydantic import BaseModel, Field


class GraphState(BaseModel):
    messages: Annotated[list[AnyMessage], operator.add]
    error_messages: Annotated[list[str], operator.add] | None = Field(
        default=None
    )
