from fastapi import FastAPI
from routers import user_router, product_router, category_router, subcategory_router, order_router, order_item_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(subcategory_router)
app.include_router(order_router)
app.include_router(order_item_router)

















