# Challenge 1:
from pydantic import BaseModel, Field, EmailStr, computed_field

class BlogPost(BaseModel):
    title: str
    content: str

    @computed_field
    @property
    def word_count(self) -> int:
        return len(self.content.split())
    
post = BlogPost(title="My First Post", content="This is the content of my first post.")
print(post)  

# Challenge 2:
from pydantic import field_validator
from datetime import datetime

class ApiResponse(BaseModel):
    created_at: datetime

    @field_validator("created_at", mode="before")
    def parse_datetime(cls, value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        elif isinstance(value, int):
            return datetime.fromtimestamp(value)
        raise ValueError("Invalid datetime format")
    
date1 = ApiResponse(created_at="2023-10-01T12:00:00")
date2 = ApiResponse(created_at=1696156800)
print(date1)
print(date2)

from pydantic import StrictBool, StrictInt, StrictFloat, StrictStr

class Config(BaseModel):
    debug: StrictBool = False
    timeout: StrictInt = 30
    threshold: StrictFloat = 0.5

valid_config = Config(debug=True, timeout=10, threshold=0.75)
# valid_config2 = Config(debug="True", timeout="10", threshold="0.75")  # This will raise a validation error
print(valid_config)

# Challenge 3:
class User(BaseModel):
    username: StrictStr
    age: StrictInt
    is_active: StrictBool = True

user = User(username="john_doe", age=30, is_active=True, email="gmail.com")
print(user)  # This will raise a validation error because email is not a valid field in User model

class StrictUser(BaseModel):
    username: StrictStr
    age: StrictInt
    is_active: StrictBool = True

    class Config:
        extra = "forbid"

user = StrictUser(username="john_doe", age=30, is_active=True)  # This will work
# user2 = StrictUser(username="john_doe", age=30, is_active=True, email="gmail.com")  # This will raise a validation error
print(user)  # This will work

# Challenge 4:
from pydantic import validate_call

@validate_call
async def process_payment(amount: float):
    if amount <= 0:
        raise ValueError("Payment amount must be positive.")
    return f"Processed payment of ${amount:.2f}"

# Example usage
import asyncio
asyncio.run(process_payment(50.75))  # Works!
# asyncio.run(process_payment(-10))  # Raises error


