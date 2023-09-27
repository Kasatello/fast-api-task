from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

import db
from schemas import Product, ProductCreate
from crud import create_product, get_product

app = FastAPI()


def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


@app.post("/products/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return get_product(db, product_id)


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    return update_product(db, product_id, product)


@app.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)
