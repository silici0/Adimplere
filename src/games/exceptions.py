from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


async def validation_exception_handler(_: Request,
                                       exc: RequestValidationError):
    error = "; ".join([f"{e['loc'][-1]}: {e['msg']}" for e in exc.errors()])
    content = dict(status=status.HTTP_400_BAD_REQUEST, error=error)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(content),
    )
