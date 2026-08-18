from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


from schemas.subcategory import SubcategoryRequestSchema
from repositories import SubcategoryRepository



class SubcategoryService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.subcategory_repository = SubcategoryRepository(db)


    async def create_subcategory(self, data: SubcategoryRequestSchema):
        return await self.subcategory_repository.create_subcategory(data.model_dump())


    async def get_subcategory_by_id(self, subcategory_id: int):
        subcategory = await self.subcategory_repository.get_subcategory_by_id(subcategory_id)
        if not subcategory:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Subcategory with id {subcategory_id} not found")
        return subcategory


    async def update_subcategory(self, subcategory_id: int, data: SubcategoryRequestSchema):
        subcategory = await self.subcategory_repository.update_subcategory(subcategory_id, data.model_dump())
        if not subcategory:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Subcategory with id {subcategory_id} not found")
        return subcategory

    async def delete_subcategory(self, subcategory_id: int):
        subcategory = await self.subcategory_repository.delete_subcategory(subcategory_id)
        if not subcategory:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Subcategory with id {subcategory_id} not found")
        return subcategory
