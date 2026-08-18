from pydantic import BaseModel, ConfigDict


class UserRequestSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    email: str = None
    hashed_password: str = None


class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str = None
















