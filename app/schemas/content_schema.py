from pydantic import BaseModel


class ContentInput(BaseModel):
    content: str