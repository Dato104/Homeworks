from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


from schemas.order import OrderRequestSchema
from repositories import OrderRepository



class OrderService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.order_repository = OrderRepository(db)


    async def create_order(self, data: OrderRequestSchema):
        return await self.order_repository.create_order(data.model_dump())


    async def get_order_by_id(self, order_id: int):
        order = await self.order_repository.get_order_by_id(order_id)
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {order_id} not found")
        return order


    async def update_order(self, order_id: int, data: OrderRequestSchema):
        order = await self.order_repository.update_order(order_id, data.model_dump())
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {order_id} not found")
        return order

    async def delete_order(self, order_id: int):
        order = await self.order_repository.delete_order(order_id)
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {order_id} not found")
        return order