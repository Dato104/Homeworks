from fastapi import FastAPI
from routers import user_router, category_router, subcategory_router, order_router, order_item_router, product_router, auth_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from core import CorrelationIdMiddleware


app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.add_middleware(CorrelationIdMiddleware)


app.include_router(user_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1")
app.include_router(category_router, prefix="/api/v1")
app.include_router(subcategory_router, prefix="/api/v1")
app.include_router(order_router, prefix="/api/v1")
app.include_router(order_item_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v2")



