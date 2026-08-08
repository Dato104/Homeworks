from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.order_item import OrderItemRequestSchema,OrderItemResponseSchema
from services.order_item import OrderItemService
from repositories.order_item import OrderItemRepository


router = APIRouter(prefix="/order_items", tags=["Order_items"])

@router.post("/", response_model=OrderItemResponseSchema)
async def create_order_item(data: OrderItemRequestSchema, db: AsyncSession = Depends(get_db)):
    order_item_serv = OrderItemService(db)
    order_item = await order_item_serv.create_order_item(data)
    return order_item

@router.get("/", response_model=List[OrderItemResponseSchema])
async def get_all_order_items(db: AsyncSession = Depends(get_db)):
    order_item_rep = OrderItemRepository(db)
    order_item = await order_item_rep.get_all_order_items()
    return order_item

@router.get("/{order_item_id}", response_model=OrderItemResponseSchema)
async def get_order_item(order_item_id: int, db: AsyncSession = Depends(get_db)):
    order_item_serv = OrderItemService(db)
    order_item = await order_item_serv.get_order_item_by_id(order_item_id)
    return order_item

@router.put("/{order_item_id}", response_model=OrderItemResponseSchema)
async def update_order_item(order_item_id: int, data: OrderItemRequestSchema, db: AsyncSession = Depends(get_db)):
    order_item_serv = OrderItemService(db)
    order_item = await order_item_serv.update_order_item(order_item_id, data)
    return order_item

@router.delete("/{order_item_id}", response_model=OrderItemResponseSchema)
async def delete_order_item(order_item_id: int, db: AsyncSession = Depends(get_db)):
    order_item_serv = OrderItemService(db)
    order_item = await order_item_serv.delete_order_item(order_item_id)
    return order_item