from fastapi import APIRouter, Depends
from utils.responses import success
from module.authentication.schemas import SignIn
from module.user.models import User
from sqlalchemy.orm import Session
from config.databases import database
from module.authentication.services import create_token

auth_routes = APIRouter(prefix='/auth')

@auth_routes.post('/login')
def login(dto: SignIn, db: Session = Depends(database)):
    user = db.query(User).filter(User.phoneNumber == dto.phoneNumber).first()
    if user is None: return success('fail')
    if user.password != dto.password: return success('password not match')
    dto_dict = dict(dto)
    token = create_token(dto_dict)
    return success(token)