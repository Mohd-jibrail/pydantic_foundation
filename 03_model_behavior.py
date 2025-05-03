from pydantic import BaseModel, field_validator, model_validator, computed_field # type: ignore

class User(BaseModel):
    username: str

    @field_validator('username')
    def check_username(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be at least 3 characters long')
        return v
    
user = User(username='john')
print(user)  # Output: joh

class SignUpData(BaseModel):
    password: str
    password_repeat: str

    @model_validator(mode='after')
    def check_passwords(cls, values):
        if values.password != values.password_repeat:
            raise ValueError('Passwords do not match')
        return values
    
signup = SignUpData(password='1234', password_repeat='1234')
print(signup)  # Output: password='1234' password_repeat='1234'

class Product(BaseModel):
    name: str
    price: float
    discount: float = 0.0

    @computed_field
    def final_price(self) -> float:
        return self.price * (1 - self.discount / 100)
product = Product(name='Laptop', price=1000, discount=10)
print(product)  # Output: 900.0

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int
    rate_per_night: float
    @computed_field
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
booking = Booking(user_id=1, room_id=101, nights=3, rate_per_night=100.0)   
print(booking)  # Output: 300.0
