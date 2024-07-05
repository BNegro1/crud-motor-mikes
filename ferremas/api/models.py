from django.db import models
from pydantic import BaseModel
from typing import List
from datetime import datetime

class Price(BaseModel):
    date: datetime
    value: float

class Product(BaseModel):
    product_code: str
    brand: str
    code: str
    name: str
    prices: List[Price]
    stock: int
