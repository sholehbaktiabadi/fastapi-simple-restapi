from typing import Annotated
from fastapi import Depends
from jose import JWTError, jwt
from config.envloaders import JWT_SECRET, JWT_ALGORITHM

from fastapi.security import OAuth2PasswordBearer
from utils.exceptions import CustomException
from const.response_msg import Error

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")

def authorization(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return token
    except JWTError:
        raise CustomException(status=401, message=Error.UNAUTHORIZED)