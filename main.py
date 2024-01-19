from config.envloaders import APP_PORT
from fastapi import FastAPI
from user.routes import router
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return { "status": "it was a nice" }

app.include_router(router)

if __name__ == "__main__":
    port = int(APP_PORT)
    config = uvicorn.Config("main:app", port=port, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()