from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    email: str

class CreateUser(BaseModel):
    name: str
    email: str