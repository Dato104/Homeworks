from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


from schemas.user import UserRequestSchema
from repositories import UserRepository



class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repository = UserRepository(db)


    async def create_user(self, data: UserRequestSchema):
        return await self.user_repository.create_user(data.model_dump())


    async def get_user_by_id(self, user_id: int):
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
        return user


    async def update_user(self, user_id: int, data: UserRequestSchema):
        user = await self.user_repository.update_user(user_id, data.model_dump())
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
        return user

    async def delete_user(self, user_id: int):
        user = await self.user_repository.delete_user(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
        return user
















