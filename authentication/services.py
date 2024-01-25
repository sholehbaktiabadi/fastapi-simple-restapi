from datetime import datetime, timezone, timedelta
from config.envloaders import JWT_EXPIRED_TIME, JWT_SECRET, JWT_ALGORITHM
from jose import jwt

def create_token(user: dict):
    user_encode = user.copy()
    expired = datetime.now(timezone.utc) + timedelta(minutes=int(JWT_EXPIRED_TIME))
    user_encode.update({ "exp": expired })
    token = jwt.encode(user_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token
    
