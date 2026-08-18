from sqlalchemy.ext.asyncio import AsyncSession
from models import Product
from sqlalchemy import select




class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_product(self, data: dict):
         product = Product(**data)
         self.db.add(product)
         await self.db.commit()
         return product

    async def get_all_products(self):
        products = select(Product)
        result = await self.db.scalars(products)
        return result.all()

    async def get_product_by_id(self, product_id: int):
        product = select(Product).where(Product.id == product_id)
        result = await self.db.scalars(product)

        product = result.first()
        return product

    async def update_product(self, product_id: int, data: dict):
        product = await self.get_product_by_id(product_id)
        for key, value in data.items():
            setattr(product, key, value)

        await self.db.commit()
        return product

    async def delete_product(self, product_id: int):
        product = await self.get_product_by_id(product_id)

        await self.db.delete(product)
        await self.db.commit()
        return product
















































