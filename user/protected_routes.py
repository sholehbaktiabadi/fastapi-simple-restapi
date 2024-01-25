from fastapi import APIRouter
from utils.responses import success

protected_router = APIRouter(prefix="/protected")

@protected_router.get('')
def protected():
    return success("protected")
