from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


from schemas.category import CategoryRequestSchema
from repositories import CategoryRepository



class CategoryService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.category_repository = CategoryRepository(db)


    async def create_category(self, data: CategoryRequestSchema):
        return await self.category_repository.create_category(data.model_dump())


    async def get_category_by_id(self, category_id: int):
        category = await self.category_repository.get_category_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")
        return category


    async def update_category(self, category_id: int, data: CategoryRequestSchema):
        category = await self.category_repository.update_category(category_id, data.model_dump())
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")
        return category

    async def delete_category(self, category_id: int):
        category = await self.category_repository.delete_category(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")
        return category
