from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.user import UserResponseSchema, UserRequestSchema
from services.user import UserService
from repositories.user import UserRepository


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponseSchema)
async def create_user(data: UserRequestSchema, db: AsyncSession = Depends(get_db)):
    user_rep = UserService(db)
    user = await user_rep.create_user(data)
    return user

@router.get("/", response_model=List[UserResponseSchema])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    user_rep = UserRepository(db)
    users = await user_rep.get_all_users()
    return users

@router.get("/{user_id}", response_model=UserResponseSchema)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user_serv = UserService(db)
    user = await user_serv.get_user_by_id(user_id)
    return user

@router.put("/{user_id}", response_model=UserResponseSchema)
async def update_user(user_id: int, data: UserRequestSchema, db: AsyncSession = Depends(get_db)):
    user_serv = UserService(db)
    user = await user_serv.update_user(user_id, data)
    return user

@router.delete("/{user_id}", response_model=UserResponseSchema)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user_serv = UserService(db)
    user = await user_serv.delete_user(user_id)
    return user












