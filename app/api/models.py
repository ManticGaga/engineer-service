from pydantic import BaseModel
from typing import List, Optional

class EngineerIn(BaseModel):
    name: str
    phone: str
    pay: str
    genre: str


class EngineerOut(EngineerIn):
    id: int
