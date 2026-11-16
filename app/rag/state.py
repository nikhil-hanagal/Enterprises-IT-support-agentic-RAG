from typing import Literal
from typing_extensions import TypedDict
from pydantic import BaseModel, Field


class RouteDecision(BaseModel):
    route: Literal["kb", "direct"] = Field(
        description="Use kb for company IT support questions and direct for greetings."
    )


class EvidenceGrade(BaseModel):
    grade: Literal["good", "weak"] = Field(
        description="Good means the evidence is sufficient. Weak means it is insufficient."
    )


class AgentState(TypedDict):
    question: str
    current_query: str
    kb_docs: list
    web_results: str
    kb_grade: str
    web_grade: str
    answer: str
    source_used: str
    retry_count: int
    trace: list
    citations: list