from pydantic import BaseModel


class UserRegistration(BaseModel):
    username: str
    login: str
    email: str
    password_input: str
    confirm_password: str


class UserEntrance(BaseModel):
    email: str
    password: str
