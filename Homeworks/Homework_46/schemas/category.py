from pydantic import BaseModel, ConfigDict


class CategoryRequestSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str




class CategoryResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
