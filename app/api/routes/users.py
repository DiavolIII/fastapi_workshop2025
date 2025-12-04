from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.users import User, UserCreate, UserOut
from app.repositories.users import create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut)
async def create_user_endpoint(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_db)
):
    user = await create_user(session, user_in.username, user_in.password)
    return user