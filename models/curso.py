from typing import Optional
from pydantic import BaseModel
import random

class Curso(BaseModel):
    id: Optional[int] = random.randint(10000, 1000000)
    titulo: str
    aulas: int
    horas: int