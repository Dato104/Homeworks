from fastapi import HTTPException
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from core.security import create_access_token, create_refresh_token, decode_token, revoke_token, is_token_blacklisted, hash_password, verify_password
from schemas import UserLoginRequest, TokenPair, TokenRefresh, UserRegisterRequest
from repositories import UserRepository



class AuthService:
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def register(self, user: UserRegisterRequest):
        existing = await self.repository.get_user_by_email(user.email)
        if existing is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        hashed_password = hash_password(user.password)

        user = await self.repository.create_user({"name": user.name, "email": user.email, "hashed_password": hashed_password })
        return user

    async def login(self, data: UserLoginRequest):
        user = await self.repository.get_user_by_email(email=data.email)

        hashed_password = user.hashed_password
        plain_password = data.password
        password_ok = verify_password(plain_password, hashed_password)

        if user is None or not password_ok or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token = await self.issue_token(user)
        return token


    async def logout(self, token: str):
        try:
            payload = decode_token(token)
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired refresh token",
            )
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Expected refresh token",
            )

        jti = payload.get("jti")
        if jti is not None:
            revoke_token(jti)


    async def refresh(self, refresh_token: str):
        try:
            payload = decode_token(refresh_token)
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired refresh token",
            )

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Expected refresh token",
            )

        jti = payload.get("jti")

        if jti is not None:
            blacklisted = is_token_blacklisted(jti)
            if blacklisted:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Blacklisted token",
                )

        user = await self.repository.get_user_by_id(int(payload.get("sub")))
        if user is None or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User no longer exists or is inactive",
            )

        token = await self.issue_token(user)
        return TokenRefresh(access_token=token.access_token)





    async def issue_token(self, user, refresh=False):
        token_data = {"sub": str(user.id), "email": user.email, "name": user.name, "is_active": user.is_active}

        access_token = create_access_token(data=token_data)

        refresh_token = None

        if not refresh:
            refresh_token = create_refresh_token(data=token_data)


        return TokenPair(
            access_token=access_token,
            refresh_token=refresh_token,
        )































