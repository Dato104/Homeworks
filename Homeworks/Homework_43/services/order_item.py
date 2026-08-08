from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


from schemas.order_item import OrderItemRequestSchema
from repositories import OrderItemRepository



class OrderItemService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.order_item_repository = OrderItemRepository(db)


    async def create_order_item(self, data: OrderItemRequestSchema):
        return await self.order_item_repository.create_order_item(data.model_dump())


    async def get_order_item_by_id(self, order_item_id: int):
        order_item = await self.order_item_repository.get_order_item_by_id(order_item_id)
        if not order_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order_item with id {order_item_id} not found")
        return order_item


    async def update_order_item(self, order_item_id: int, data: OrderItemRequestSchema):
        order_item = await self.order_item_repository.update_order_item(order_item_id, data.model_dump())
        if not order_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order_item  with id {order_item_id} not found")
        return order_item

    async def delete_order_item(self, order_item_id: int):
        order_item = await self.order_item_repository.delete_order_item(order_item_id)
        if not order_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order_item  with id {order_item_id} not found")
        return order_item