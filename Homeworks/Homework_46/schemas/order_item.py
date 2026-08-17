from pydantic import BaseModel, ConfigDict


class OrderItemRequestSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
    order_id: int
    quantity: int




class OrderItemResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    order_id: int
    quantity: int