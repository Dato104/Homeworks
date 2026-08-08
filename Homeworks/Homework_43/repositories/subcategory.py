from sqlalchemy.ext.asyncio import AsyncSession
from models import SubCategory
from sqlalchemy import select




class SubcategoryRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_subcategory(self, data: dict):
         subcategory = SubCategory(**data)
         self.db.add(subcategory)
         await self.db.commit()
         return subcategory

    async def get_all_subcategory(self):
        subcategories = select(SubCategory)
        result = await self.db.scalars(subcategories)
        return result.all()

    async def get_subcategory_by_id(self, subcategory_id: int):
        subcategory = select(SubCategory).where(SubCategory.id == subcategory_id)
        result = await self.db.scalars(subcategory)

        subcategory = result.first()
        return subcategory

    async def update_subcategory(self, subcategory_id: int, data: dict):
        subcategory = await self.get_subcategory_by_id(subcategory_id)
        for key, value in data.items():
            setattr(subcategory, key, value)

        await self.db.commit()
        return subcategory

    async def delete_subcategory(self, subcategory_id: int):
        subcategory = await self.get_subcategory_by_id(subcategory_id)

        await self.db.delete(subcategory)
        await self.db.commit()
        return subcategory