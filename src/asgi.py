import logging

from fastapi import FastAPI, APIRouter, status, Request
from src import config
from starlette.middleware.cors import CORSMiddleware
from src.games.entrypoints.api import router as games_router
from fastapi.exceptions import RequestValidationError
from src.games.exceptions import validation_exception_handler
import time
from fastapi_utils.timing import add_timing_middleware, record_timing

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app(debug: bool = False) -> FastAPI:
    app = FastAPI(title=config.get_app_name(), debug=debug)
    add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

    origins = ["*"]

    app.include_router(games_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_exception_handler(
        RequestValidationError, validation_exception_handler
    )
    return app
