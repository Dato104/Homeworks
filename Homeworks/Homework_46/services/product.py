from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


from schemas.product import ProductRequestSchema
from repositories import ProductRepository



class ProductService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.product_repository = ProductRepository(db)


    async def create_product(self, data: ProductRequestSchema):
        return await self.product_repository.create_product(data.model_dump())


    async def get_product_by_id(self, product_id: int):
        product = await self.product_repository.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
        return product


    async def update_product(self, product_id: int, data: ProductRequestSchema):
        product = await self.product_repository.update_product(product_id, data.model_dump())
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
        return product

    async def delete_product(self, product_id: int):
        product = await self.product_repository.delete_product(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
        return product
