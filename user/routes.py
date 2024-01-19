from fastapi import APIRouter, Depends
from utils.responses import response
from sqlalchemy import update
from sqlalchemy.orm import Session
from config.databases import SessionLocal
from user.models import User
from user.schemas import UserCreateSchema, UserUpdateSchema

router = APIRouter(prefix="/user")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('')
def getAll(db: Session = Depends(get_db)):
    data = db.query(User).all()
    return response(data)

@router.get('/{id}')
def getOne(id: int, db: Session = Depends(get_db)):
    selected = db.query(User).filter(User.id == id).first()
    if selected is not None:
        return response(selected)
    return response("not found", 400)

@router.delete('/{id}')
def getOne(id: int, db: Session = Depends(get_db)):
    selected = db.query(User).filter(User.id == id).first()
    if selected is not None:
        db.delete(selected)
        db.commit()
        return response(selected)
    return response("not found", 400)
        

@router.post('')
def create(user: UserCreateSchema, db: Session = Depends(get_db)):
    newEntity = User(name=user.name, age=user.age)
    db.add(newEntity)
    db.commit()
    db.refresh(newEntity)
    return response(newEntity)

@router.patch('/{id}')
def updateUser(id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
        obj = user.model_dump(exclude_none=True)
        upd = update(User)
        val = upd.values(obj)
        cond = val.where(User.id == id)
        db.execute(cond)
        return response("updated")
