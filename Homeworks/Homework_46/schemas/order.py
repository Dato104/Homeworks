from pydantic import BaseModel, ConfigDict


class OrderRequestSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


    user_id: int
    total: float




class OrderResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    total: float