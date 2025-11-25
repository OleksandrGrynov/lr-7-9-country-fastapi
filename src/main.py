import logging

from fastapi import FastAPI

from src.core.logging_config import setup_logging
from src.core.sentry import init_sentry
from src.external_api.router import router as external_router

setup_logging()
init_sentry()

app = FastAPI(
    title="Country API Integration Lab",
    description="Country API Integration Lab",
    version="0.1.0",
)

app.include_router(external_router)


@app.get("/", tags=["default"])
def root():
    return {"message": "Country API lab is running"}


@app.get("/sentry-debug", tags=["default"])
def sentry_debug():
    logging.getLogger(__name__).info("[ROOT][SENTRY-DEBUG] Trigger division by zero")
    1 / 0
    return {"status": "ok"}
