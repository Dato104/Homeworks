from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.category import CategoryRequestSchema, CategoryResponseSchema
from services.category import CategoryService
from repositories.category import CategoryRepository


router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponseSchema)
async def create_category(data: CategoryRequestSchema, db: AsyncSession = Depends(get_db)):
    category_serv = CategoryService(db)
    category = await category_serv.create_category(data)
    return category

@router.get("/", response_model=List[CategoryResponseSchema])
async def get_all_category(db: AsyncSession = Depends(get_db)):
    product_rep = CategoryRepository(db)
    category = await product_rep.get_all_category()
    return category

@router.get("/{category_id}", response_model=CategoryResponseSchema)
async def get_category(category_id: int, db: AsyncSession = Depends(get_db)):
    category_serv = CategoryService(db)
    category = await category_serv.get_category_by_id(category_id)
    return category

@router.put("/{category_id}", response_model=CategoryResponseSchema)
async def update_category(category_id: int, data: CategoryRequestSchema, db: AsyncSession = Depends(get_db)):
    category_serv = CategoryService(db)
    category = await category_serv.update_category(category_id, data)
    return category

@router.delete("/{category_id}", response_model=CategoryResponseSchema)
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    category_serv = CategoryService(db)
    category = await category_serv.delete_category(category_id)
    return category