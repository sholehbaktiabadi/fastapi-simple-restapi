from fastapi import APIRouter, Depends
from utils.responses import success, error
from module.authentication.schemas import SignIn
from module.user.models import User
from sqlalchemy.orm import Session
from config.databases import database
from module.authentication.services import create_token
from utils.bcrypts import verify_hash_password
from const.response_msg import Error

auth_routes = APIRouter(prefix='/auth')

@auth_routes.post('/login')
def login(dto: SignIn, db: Session = Depends(database)):
    user = db.query(User).filter(User.phoneNumber == dto.phoneNumber).first()
    print(user)
    if user is None: return error(Error.NOT_REGISTERED, 400)
    if not verify_hash_password(dto.password, user.password):
        return error(Error.INVALID_CREDENTIAL, 403)
    dto_dict = dict(dto)
    token = create_token(dto_dict)
    return success(token)