from fastapi import APIRouter

router = APIRouter(prefix="/project")

@router.get('')
def root():
    return { "massage": "hai there tihs is project" }

@router.get('/{id}')
def param(id: int):
    return { "massage": id }