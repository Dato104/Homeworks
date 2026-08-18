from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base


class OrderItem(Base):
    __tablename__ = 'order_items'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    product = relationship("Product", back_populates="order_items")
    order = relationship("Order", back_populates="order_items")











