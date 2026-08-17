from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.subcategory import SubcategoryRequestSchema, SubcategoryResponseSchema
from services.subcategory import SubcategoryService
from repositories.subcategory import SubcategoryRepository


router = APIRouter(prefix="/subcategories", tags=["Subcategories"])

@router.post("/", response_model=SubcategoryResponseSchema)
async def create_subcategory(data: SubcategoryRequestSchema, db: AsyncSession = Depends(get_db)):
    subcategory_serv = SubcategoryService(db)
    subcategory = await subcategory_serv.create_subcategory(data)
    return subcategory

@router.get("/", response_model=List[SubcategoryResponseSchema])
async def get_all_subcategory(db: AsyncSession = Depends(get_db)):
    subcategory_rep = SubcategoryRepository(db)
    subcategory = await subcategory_rep.get_all_subcategory()
    return subcategory

@router.get("/{subcategory_id}", response_model=SubcategoryResponseSchema)
async def get_subcategory(subcategory_id: int, db: AsyncSession = Depends(get_db)):
    subcategory_serv = SubcategoryService(db)
    subcategory = await subcategory_serv.get_subcategory_by_id(subcategory_id)
    return subcategory

@router.put("/{subcategory_id}", response_model=SubcategoryResponseSchema)
async def update_subcategory(subcategory_id: int, data: SubcategoryRequestSchema, db: AsyncSession = Depends(get_db)):
    subcategory_serv = SubcategoryService(db)
    subcategory = await subcategory_serv.update_subcategory(subcategory_id, data)
    return subcategory

@router.delete("/{subcategory_id}", response_model=SubcategoryResponseSchema)
async def delete_subcategory(subcategory_id: int, db: AsyncSession = Depends(get_db)):
    subcategory_serv = SubcategoryService(db)
    subcategory = await subcategory_serv.delete_subcategory(subcategory_id)
    return subcategory