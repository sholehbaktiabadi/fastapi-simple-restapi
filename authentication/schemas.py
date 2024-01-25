from pydantic import BaseModel
from typing import Optional

class SignIn(BaseModel):
    phoneNumber: Optional[str] = None
    password: Optional[str] = None

    class Config:
        from_attributes = True
    