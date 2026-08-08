
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
from sqlalchemy import String, Float, ForeignKey


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("subcategories.id"), nullable=False)

    category = relationship("Category", back_populates="products")
    subcategory = relationship("SubCategory", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")


