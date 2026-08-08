from sqlalchemy.ext.asyncio import AsyncSession
from models import OrderItem
from sqlalchemy import select




class OrderItemRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_order_item(self, data: dict):
         order_item = OrderItem(**data)
         self.db.add(order_item)
         await self.db.commit()
         return order_item

    async def get_all_order_items(self):
        order_item = select(OrderItem)
        result = await self.db.scalars(order_item)
        return result.all()

    async def get_order_item_by_id(self, order_item_id: int):
        order_item = select(OrderItem).where(OrderItem.id == order_item_id)
        result = await self.db.scalars(order_item)

        order_item = result.first()
        return order_item

    async def update_order_item(self, order_item_id: int, data: dict):
        order_item = await self.get_order_item_by_id(order_item_id)
        for key, value in data.items():
            setattr(order_item, key, value)

        await self.db.commit()
        return order_item

    async def delete_order_item(self, order_item_id: int):
        order_item = await self.get_order_item_by_id(order_item_id)

        await self.db.delete(order_item)
        await self.db.commit()
        return order_item