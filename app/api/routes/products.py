from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.products import Product, ProductCreate, ProductUpdate, ProductOut
from app.repositories.products import (
    get_product_by_id,
    create_product,
    update_product
)

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: int, session: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    return product

@router.post("/", response_model=ProductOut)
async def create_product_endpoint(
    product_in: ProductCreate,
    session: AsyncSession = Depends(get_db)
):
    product = await create_product(session, product_in)
    return product

@router.put("/{product_id}", response_model=ProductOut)
async def update_product_endpoint(
    product_id: int,
    product_in: ProductUpdate,
    session: AsyncSession = Depends(get_db)
):
    product = await get_product_by_id(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    updated_product = await update_product(session, product, product_in)
    return updated_product