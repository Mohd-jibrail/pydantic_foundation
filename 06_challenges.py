from pydantic import BaseModel, EmailStr# type: ignore

# Challenge 1: Create a Pydantic model for a user with fields: name (str), age (int), and email (EmailStr).
class User(BaseModel):
    name: str
    age: int | None = None
    email: EmailStr | None = None

invalid_user = User(name="John Doe", age=30, email="invalide@gmail.com")
print(invalid_user) 

# Challenge 2: 
from pydantic import field_validator # type: ignore

class Product(BaseModel):
    name: str
    price: float
    discount: float

    @field_validator('price')
    def check_price(cls, v):
        if (0 > v):
            raise ValueError('Price must be a positive number')
        return v

    @field_validator('discount')
    def check_discount(cls, v):
        if (0 <= v >= 100):
            raise ValueError('Discount must be between 0 and 100')
        return v
    
product = Product(name="Laptop", price=10, discount=10)
print(product)  

from pydantic import UUID4, computed_field # type: ignore


# challenge 3: 
class Order(BaseModel):
    order_id: UUID4
    products : list[Product]

    @computed_field
    @property
    def total_price(self) -> float:
        return sum(product.price for product in self.products)
    
from uuid import uuid4

order = Order(order_id=uuid4(), products=[product])

