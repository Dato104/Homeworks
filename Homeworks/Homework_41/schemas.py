from pydantic import BaseModel, ConfigDict


class TripCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    destination: str
    country: str = None
    days: int
    budget: int
    is_completed: bool

class TripResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    destination: str
    country: str = None
    days: int
    budget: int
    is_completed: bool













