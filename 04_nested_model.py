from pydantic import BaseModel #type:ignore 
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None
    address: Address

class Comment(BaseModel):
    id: int
    user_id: int
    content: str
    replies: Optional[List['Comment']] = None # type: ignore

Comment.model_rebuild() # Rebuild the model to ensure it is up to date

address = Address(
    street="123 Main St",
    city="Anytown",
    state="CA",
    zip_code="12345"
)
user = User(
    id=1,
    name="John Doe",
    email="mjibrail34@gmail.com",
    address=address
)   

comment = Comment( 
    id=1,
    user_id=user.id,
    content="This is a comment.",
    replies=[
        Comment(
            id=2,
            user_id=user.id,
            content="This is a reply.",
            replies=[
                Comment(
                    id=3,
                    user_id=user.id,
                    content="This is a nested reply."
                )
            ]
        )
    ]
)
print(comment)

# TODO: Create  Course Model
# Each Course has modules 
# Each Module has lessons
# Each Lesson has a title and content

class Lesson(BaseModel):
    title: str
    content: str

class Module(BaseModel):
    title: str
    lessons: List[Lesson]

class Course(BaseModel):
    title: str
    description: str
    modules: List[Module]

course = Course(
    title="Python Programming",
    description="Learn Python from scratch.",
    modules=[
        Module(
            title="Introduction to Python",
            lessons=[
                Lesson(
                    title="What is Python?",
                    content="Python is a programming language."
                ),
                Lesson(
                    title="Setting up Python",
                    content="Install Python and set up your environment."
                )
            ]
        ),
        Module(
            title="Advanced Python",
            lessons=[
                Lesson(
                    title="Decorators",
                    content="Learn about decorators in Python."
                )
            ]
        )
    ]
)
print(course)