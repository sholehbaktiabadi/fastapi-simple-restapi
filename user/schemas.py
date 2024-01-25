from pydantic import BaseModel
from typing import Optional

class UserCreateSchema(BaseModel):
    name: str
    age: int
    
    class Config:
        from_attributes = True

class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    
    class Config:
        from_attributes = True