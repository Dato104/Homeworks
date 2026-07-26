from sqlalchemy import create_engine, String, Integer, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, relationship,Mapped, mapped_column
from datetime import datetime


engine = create_engine(
    "postgresql+psycopg2://postgres:datobase003@localhost:5432/homework"
)

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(70), unique=True)

    orders = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    order_date: Mapped[datetime] = mapped_column(server_default=func.now())

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column(Integer, nullable=False)

    order_items = relationship("OrderItem", back_populates="product")


class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")


Base.metadata.create_all(engine)


