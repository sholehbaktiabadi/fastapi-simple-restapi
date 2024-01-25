from fastapi import APIRouter, Depends
from utils.responses import success
from sqlalchemy import update
from sqlalchemy.orm import Session
from config.databases import database
from module.user.models import User
from module.user.schemas import UserCreateSchema, UserUpdateSchema

user_router = APIRouter(prefix="/user")

@user_router.get('')
def getAll(db: Session = Depends(database)):
    data = db.query(User).all()
    return success(data)

@user_router.get('/{id}')
def getOne(id: int, db: Session = Depends(database)):
    selected = db.query(User).filter(User.id == id).first()
    if selected is not None:
        return success(selected)
    return success("not found", 400)

@user_router.delete('/{id}')
def getOne(id: int, db: Session = Depends(database)):
    selected = db.query(User).filter(User.id == id).first()
    if selected is not None:
        db.delete(selected)
        db.commit()
        return success(selected)
    return success("not found", 400)
        

@user_router.post('')
def create(user: UserCreateSchema, db: Session = Depends(database)):
    newEntity = User(name=user.name, age=user.age)
    db.add(newEntity)
    db.commit()
    db.refresh(newEntity)
    return success(newEntity)

@user_router.patch('/{id}')
def updateUser(id: int, user: UserUpdateSchema, db: Session = Depends(database)):
        obj = user.model_dump(exclude_none=True)
        upd = update(User)
        val = upd.values(obj)
        cond = val.where(User.id == id)
        db.execute(cond)
        return success("updated")
