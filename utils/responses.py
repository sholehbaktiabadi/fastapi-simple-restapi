from typing import Any
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def success(message, statusCode=status.HTTP_200_OK):
    return JSONResponse(
        status_code=statusCode,
        content=jsonable_encoder({ "statusCode": statusCode, "data": message })
    )

def error(message, statusCode: int):
    return JSONResponse(
        status_code=statusCode,
        content=jsonable_encoder({ "statusCode": statusCode, "data": message })
    )

class ErrorResponseWrapper():
    def __init__(self, statusCode: int, message: Any):
        self.statusCode= statusCode
        self.message = message