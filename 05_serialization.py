from pydantic import BaseModel, ConfigDict # type: ignore
from typing import Optional, List, Dict, Any
from datetime import datetime

class Address(BaseModel):
    street: str 
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    address: Optional[Address] = None
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={ datetime: lambda v: v.strftime("%Y-%m-%d %H:%M") },
    )


user = User(
    id=1,
    name="Mohd Jibrail",
    email="mjibrail@gmail.com",
    created_at=datetime(2024,3,15,14,30),
    address=Address(
        street="123 Main St",
        city="New York",
        zip_code="10001"
    ),
    tags=["python", "pydantic"]
)
print(type(user))
python_dict = user.model_dump()
print(python_dict)
json_str = user.model_dump_json()
print(json_str)