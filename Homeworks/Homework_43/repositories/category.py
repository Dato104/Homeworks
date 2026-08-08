from sqlalchemy.ext.asyncio import AsyncSession
from models import Category
from sqlalchemy import select




class CategoryRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_category(self, data: dict):
         category = Category(**data)
         self.db.add(category)
         await self.db.commit()
         return category

    async def get_all_category(self):
        categories = select(Category)
        result = await self.db.scalars(categories)
        return result.all()

    async def get_category_by_id(self, category_id: int):
        category = select(Category).where(Category.id == category_id)
        result = await self.db.scalars(category)

        category = result.first()
        return category

    async def update_category(self, category_id: int, data: dict):
        category = await self.get_category_by_id(category_id)
        for key, value in data.items():
            setattr(category, key, value)

        await self.db.commit()
        return category

    async def delete_category(self, category_id: int):
        category = await self.get_category_by_id(category_id)

        await self.db.delete(category)
        await self.db.commit()
        return category