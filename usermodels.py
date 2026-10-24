from pydantic import BaseModel, conint, constr
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

user1 = User(id=2, name="John doe", email="johndoe@exmaple.com")
print(user1)