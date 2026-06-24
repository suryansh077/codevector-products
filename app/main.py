from fastapi import FastAPI
from app.database import engine
from app.models import Product
from app.routes.products import router as products_router

app = FastAPI(title="CodeVector Products API")

Product.metadata.create_all(bind=engine)

app.include_router(products_router)

@app.get("/")
def home():
    return {"message": "CodeVector Task Running"}