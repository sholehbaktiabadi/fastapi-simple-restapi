from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def response(message, statusCode=status.HTTP_200_OK):
    return JSONResponse(
        status_code=statusCode,
        content=jsonable_encoder({ "statusCode": statusCode, "data": message })
    )