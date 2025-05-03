from pydantic import BaseModel, Field#type: ignore
from typing import Optional, List, Dict

class Cart(BaseModel):
    user_id: int
    item: List[str]
    quantity: Dict[str, int]

input_data = {
    "user_id": 123,
    "item": ["apple", "banana", "orange"],
    "quantity": {
        "apple": 2,
        "banana": 3,
        "orange": 1
    }
}
cart = Cart(**input_data)
print(cart)
class BlogPost(BaseModel):
    title: str
    content : str
    image_url: Optional[str] = None

input_data ={"title": "My First Blog Post",
             "content": "This is the content of my first blog post.",
             "image_url": "https://example.com/image.jpg"
}
blogPost = BlogPost(**input_data)
print(blogPost)

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="The name of the employee, must be between 3 and 50 characters.",
        example="John Doe"
    )
    department: Optional[str] ='General'
    salary: float = Field(
        ...,
        gt=10000,
        description="The salary of the employee, must be greater than 0."
    )

emp = Employee(
    id=1,
    name="John Doe",
    department="IT",
    salary=50000.0
)
print(emp)