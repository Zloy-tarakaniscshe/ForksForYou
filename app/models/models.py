from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str


class Tasks(BaseModel):
    id: int
    title: str
    description: str
    status: str
    user_id: int
