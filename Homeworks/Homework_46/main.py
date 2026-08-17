from fastapi import FastAPI
from routers import user_router, product_router, category_router, subcategory_router, order_router, order_item_router, auth_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1")
app.include_router(category_router, prefix="/api/v1")
app.include_router(subcategory_router, prefix="/api/v1")
app.include_router(order_router, prefix="/api/v1")
app.include_router(order_item_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v2")

















