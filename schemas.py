from pydantic import BaseModel

class UserBase(BaseModel):
    name : str
    age : int
    email : str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id : int

class config:
    form_attributes = True