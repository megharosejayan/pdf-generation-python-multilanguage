from pydantic import BaseModel


class Doc(BaseModel):
    id: str
    title: str
    text: str
    author: str


class DocOut(Doc):
    id: int
