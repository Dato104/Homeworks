from sqlalchemy.ext.asyncio import AsyncSession
from models import Order
from sqlalchemy import select




class OrderRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_order(self, data: dict):
         order = Order(**data)
         self.db.add(order)
         await self.db.commit()
         return order

    async def get_all_orders(self):
        orders = select(Order)
        result = await self.db.scalars(orders)
        return result.all()

    async def get_order_by_id(self, order_id: int):
        order = select(Order).where(Order.id == order_id)
        result = await self.db.scalars(order)

        order = result.first()
        return order

    async def update_order(self, order_id: int, data: dict):
        order = await self.get_order_by_id(order_id)
        for key, value in data.items():
            setattr(order, key, value)

        await self.db.commit()
        return order

    async def delete_order(self, order_id: int):
        order = await self.get_order_by_id(order_id)

        await self.db.delete(order)
        await self.db.commit()
        return order