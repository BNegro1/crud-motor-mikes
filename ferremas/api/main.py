from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from models import Product, Price
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

db = [
    Product(
        product_code="FER-12345",
        brand="Bosch",
        code="BOS-67890",
        name="Taladro Percutor Bosch",
        prices=[Price(date=datetime(2023, 5, 10, 3, 0, 0), value=89090.99)],
        stock=15
    )
]

@app.get("/products", response_model=List[Product])
def get_products():
    return db

@app.get("/products/{product_code}", response_model=Product)
def get_product(product_code: str):
    for product in db:
        if product.product_code == product_code:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/pay")
def pay():
    # Implementar la lógica de integración con Webpay
    return {"message": "Payment initiated"}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from models import Product, Price
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

db = [
    Product(
        product_code="FER-12345",
        brand="Bosch",
        code="BOS-67890",
        name="Taladro Percutor Bosch",
        prices=[Price(date=datetime(2023, 5, 10, 3, 0, 0), value=89090.99)],
        stock=15
    )
]

@app.get("/products", response_model=List[Product])
def get_products():
    return db

@app.get("/products/{product_code}", response_model=Product)
def get_product(product_code: str):
    for product in db:
        if product.product_code == product_code:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/pay")
def pay():
    # Implementar la lógica de integración con Webpay
    return {"message": "Payment initiated"}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
