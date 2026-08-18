from typing import List

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from core.dependencies import require_role, get_current_user
from models.user import UserRole, User
from schemas.order import OrderRequestSchema, OrderResponseSchema
from services.order import OrderService
from repositories.order import OrderRepository


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponseSchema)
async def create_order(
    data: OrderRequestSchema,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.CUSTOMER)),
):
    order_serv = OrderService(db)
    order = await order_serv.create_order(data, user_id=current_user.id)
    return order


@router.get("/", response_model=List[OrderResponseSchema])
async def get_all_orders(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    order_rep = OrderRepository(db)
    orders = await order_rep.get_all_orders()
    return orders


@router.get("/{order_id}", response_model=OrderResponseSchema)
async def get_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    order_serv = OrderService(db)
    order = await order_serv.get_order_by_id(order_id)

    if current_user.role != UserRole.ADMIN and order.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to view this order",
        )

    return order


@router.put("/{order_id}", response_model=OrderResponseSchema)
async def update_order(
    order_id: int,
    data: OrderRequestSchema,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    order_serv = OrderService(db)
    order = await order_serv.update_order(order_id, data)
    return order


@router.delete("/{order_id}", response_model=OrderResponseSchema)
async def delete_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    order_serv = OrderService(db)
    order = await order_serv.delete_order(order_id)
    return order