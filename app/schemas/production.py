from pydantic import BaseModel
from datetime import date

class ProductionBase(BaseModel):
    date: date
    line: str
    area: str
    capacity: float
    produced_quantity: float
    available_capacity: float

class ProductionCreate(ProductionBase):
    pass

class ProductionResponse(ProductionBase):
    id: int

    class Config:
        from_attributes = True
class ProductionUpdate(ProductionCreate):
    pass
