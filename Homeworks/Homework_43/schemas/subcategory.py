from pydantic import BaseModel, ConfigDict


class SubcategoryRequestSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    category_id: int




class SubcategoryResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    category_id: int