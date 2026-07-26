from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import select

from models import engine, Customer, Order, Product, OrderItem


Session = sessionmaker(bind=engine)
session = Session()


customers = [
    Customer(name="John", email="John@gmail.com"),
    Customer(name="Anna", email="Anna@gmail.com"),
    Customer(name="Kate", email="Kate@gmail.com"),
    Customer(name="Bob", email="Bob@gmail.com"),
    Customer(name="Patrick", email="Patrick@gmail.com"),
]

session.add_all(customers)
session.commit()


products = [
    Product(name="Laptop", price=2000),
    Product(name="Phone", price=1000),
    Product(name="Keyboard", price=300),
    Product(name="Mouse", price=200),
    Product(name="Monitor", price=400),
    Product(name="Headphones", price=100),
    Product(name="Tablet", price=150),
    Product(name="Camera", price=50),
]


session.add_all(products)
session.commit()



orders = [
    Order(customer_id=1),
    Order(customer_id=1),
    Order(customer_id=2),
    Order(customer_id=3),
    Order(customer_id=3),
]
session.add_all(orders)
session.commit()




order_items = [
    OrderItem(order_id=1, product_id=1, quantity=1),
    OrderItem(order_id=2, product_id=2, quantity=1),
    OrderItem(order_id=1, product_id=4, quantity=2),
    OrderItem(order_id=3, product_id=6, quantity=3),
    OrderItem(order_id=3, product_id=5, quantity=1),
]

session.add_all(order_items)
session.commit()



stmt = select(Customer.id, Customer.name, Customer.email)

customers = session.execute(stmt).all()
for customer in customers:
    print(f"ID: {customer.id} || Name: {customer.name} || Email: {customer.email}")



stmt = select(Customer).options(joinedload(Customer.orders)).where(Customer.id == 1)
result = session.execute(stmt).unique().all()

for row in result:
    customer = row[0]
    print(f"Customer: {customer.name}")
    for order in customer.orders:
        print(f"Order ID: {order.id}")
        print(f"Order Date: {order.order_date}")



stmt = select(OrderItem).options(joinedload(OrderItem.product)).where(OrderItem.order_id == 1)
result = session.execute(stmt).unique().scalars().all()

for order_item in result:
    print(f"Order ID: {order_item.order_id}")
    print(f"Product: {order_item.product.name}")
    print(f"Quantity: {order_item.quantity}")





customer = session.scalars(select(Customer).where(Customer.id == 1)).first()


order = Order(
    customer=customer,
)

session.add(order)



product_1 = session.scalars(select(Product).where(Product.id == 1)).first()



order_item = OrderItem(
    product=product_1,
    order=order,
    quantity=1,
)
session.add(order_item)


product_2 = session.scalars(select(Product).where(Product.id == 4)).first()

order_item = OrderItem(
    product=product_2,
    order=order,
    quantity=2,
)

session.add(order_item)

product_3 = session.scalars(select(Product).where(Product.id == 5)).first()

order_item = OrderItem(
    product=product_3,
    order=order,
    quantity=2,
)
session.add(order_item)

session.commit()



product_1 = session.scalars(select(Product).where(Product.id == 1)).first()

product_1.price = 4000
session.commit()

session.close()












