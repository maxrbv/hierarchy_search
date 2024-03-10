from pydantic import BaseModel


class IdModel(BaseModel):
    elem_id: str
