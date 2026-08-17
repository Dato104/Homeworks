from pydantic import BaseModel, ConfigDict


class ProductRequestSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    price: float
    category_id: int
    subcategory_id: int




class ProductResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    category_id: int
    subcategory_id: int