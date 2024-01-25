from fastapi.responses import JSONResponse
from config.envloaders import APP_PORT
from fastapi import FastAPI, Request, Depends
from module.user.routes import user_router
from module.user.protected_routes import protected_router
from module.authentication.routes import auth_routes
from utils.exceptions import CustomException
from module.authentication.authorizations import jwt_required
from utils.responses import ErrorResponseWrapper
from const.error_types import Ok
from utils.responses import success
import uvicorn

app = FastAPI()

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    data = ErrorResponseWrapper(statusCode=exc.status, message=exc.message)
    return JSONResponse(
        status_code=exc.status,
        content=data.__dict__
    )

@app.get('/health-check')
def root():
    return success(Ok.HEALTH_CHECK)

app.include_router(user_router)
app.include_router(auth_routes)
app.include_router(protected_router, dependencies=[Depends(jwt_required)])

if __name__ == "__main__":
    port = int(APP_PORT)
    config = uvicorn.Config("main:app", port=port, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()