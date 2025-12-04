from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users import User
from app.core.security import get_password_hash

async def create_user(session: AsyncSession, username: str, password: str) -> User:
    hashed_pw = get_password_hash(password)
    user = User(username=username, hashed_password=hashed_pw)
    session.add(user)
    await session.commit()
    return user

async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    result = await session.execute(
        select(User).where(User.username == username)
    )
    return result.scalar_one_or_none()