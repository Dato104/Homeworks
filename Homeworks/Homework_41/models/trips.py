from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from database import engine


class Base(DeclarativeBase):
    pass

class Trip(Base):
    __tablename__ = 'trips'

    id: Mapped[int] = mapped_column(primary_key=True)
    destination: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=True)
    days: Mapped[int] = mapped_column(Integer)
    budget: Mapped[int] = mapped_column(Integer)
    is_completed: Mapped[bool] = mapped_column(Boolean, nullable=False)




# Base.metadata.create_all(engine)






















