from pydantic import BaseModel # type: ignore

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

input_data = { "id": "12a", "name": "Mohd Jibrail", "email": "mjibrai34@gmail.com", "is_active": True }
user = User(**input_data)
print(user)