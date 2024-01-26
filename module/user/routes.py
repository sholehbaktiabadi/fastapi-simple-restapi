from fastapi import APIRouter, Depends
from utils.responses import success, error
from sqlalchemy.orm import Session
from config.databases import database
from module.user.models import User
from module.user.schemas import UserCreateSchema, UserUpdateSchema
from utils.bcrypts import hash_password
from const.response_msg import Error, Ok

user_router = APIRouter(prefix="/user")

@user_router.post('')
def create(user: UserCreateSchema, db: Session = Depends(database)):
    hashed_password = hash_password(user.password)
    new_entity = User(name=user.name, age=user.age, password=hashed_password, phoneNumber=user.phoneNumber)
    db.add(new_entity)
    db.commit()
    return success(Ok.SUCCESS)

@user_router.get('')
def getAll(db: Session = Depends(database)):
    data = db.query(User)._get_options(only_load_props=User.select).all()
    return success(data)

@user_router.get('/{id}')
def getOne(id: int, db: Session = Depends(database)):
    selected = db.query(User)._get_options(only_load_props=User.select) .filter(User.id == id).first()
    if selected is not None:
        return success(selected)
    return error(Error.NOTFOUND, 400)

user_protected_router = APIRouter(prefix="/user")

@user_protected_router.delete('/{id}')
def delete(id: int, db: Session = Depends(database)):
    selected = db.query(User).filter(User.id == id).first()
    if selected is not None:
        db.delete(selected)
        db.commit()
        return success(Ok.SUCCESS)
    return error(Error.NOTFOUND, 400)

@user_protected_router.patch('/{id}')
def update(id: int, user: UserUpdateSchema, db: Session = Depends(database)):
    obj = user.model_dump(exclude_none=True)
    db.query(User).filter(User.id == id).update(obj, synchronize_session=False)
    db.commit()
    return success(Ok.SUCCESS)