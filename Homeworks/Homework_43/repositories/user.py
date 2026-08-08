from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from sqlalchemy import select




class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, data: dict):
         user = User(**data)
         self.db.add(user)
         await self.db.commit()
         return user

    async def get_all_users(self):
        users = select(User)
        result = await self.db.scalars(users)
        return result.all()

    async def get_user_by_id(self, user_id: int):
        user = select(User).where(User.id == user_id)
        result = await self.db.scalars(user)

        user = result.first()
        return user

    async def update_user(self, user_id: int, data: dict):
        user = await self.get_user_by_id(user_id)
        for key, value in data.items():
            setattr(user, key, value)

        await self.db.commit()
        return user

    async def delete_user(self, user_id: int):
        user = await self.get_user_by_id(user_id)

        await self.db.delete(user)
        await self.db.commit()
        return user






























