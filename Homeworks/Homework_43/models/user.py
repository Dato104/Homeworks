
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from core.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(70), nullable=True, unique=True)


    orders = relationship("Order", back_populates="user")


























