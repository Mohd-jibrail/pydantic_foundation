from pydantic import BaseModel # type: ignore

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

input_data = { "id": "12", "name": "Mohd Jibrail", "email": "mjibrai34@gmail.com", "is_active": True }
user = User(**input_data)
print(user)

class Product(BaseModel):
    id: int
    name: str
    price: float
    is_available: bool = True

product = Product(id=1, name="Laptop", price=999.99, is_available=True)
print(product)