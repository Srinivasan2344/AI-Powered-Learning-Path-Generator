from pydantic import BaseModel


class QualityInput(BaseModel):
    content: str