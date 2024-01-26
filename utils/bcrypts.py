from passlib.context import CryptContext

bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(str: str):
    hashed_password = bcrypt.hash(str)
    return hashed_password

def verify_hash_password(plain_password: str, hash_password):
    return bcrypt.verify(plain_password, hash_password)
    