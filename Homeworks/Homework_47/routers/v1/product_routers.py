from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from core.dependencies import require_role, get_current_user
from models.user import UserRole, User
from schemas.product import ProductRequestSchema, ProductResponseSchema
from services.product import ProductService
from repositories.product import ProductRepository


router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponseSchema)
async def create_product(
    data: ProductRequestSchema,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    product_serv = ProductService(db)
    product = await product_serv.create_product(data)
    return product


@router.get("/", response_model=List[ProductResponseSchema])
async def get_all_products(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    product_rep = ProductRepository(db)
    products = await product_rep.get_all_products()
    return products


@router.get("/{product_id}", response_model=ProductResponseSchema)
async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    product_serv = ProductService(db)
    product = await product_serv.get_product_by_id(product_id)
    return product


@router.put("/{product_id}", response_model=ProductResponseSchema)
async def update_product(
    product_id: int,
    data: ProductRequestSchema,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    product_serv = ProductService(db)
    product = await product_serv.update_product(product_id, data)
    return product


@router.delete("/{product_id}", response_model=ProductResponseSchema)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    product_serv = ProductService(db)
    product = await product_serv.delete_product(product_id)
    return product