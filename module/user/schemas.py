from pydantic import BaseModel
from typing import Optional

class UserCreateSchema(BaseModel):
    name: str
    phoneNumber: str
    password: str
    age: Optional[int] = None
    
    class Config:
        from_attributes = True

class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    
    class Config:
        from_attributes = True