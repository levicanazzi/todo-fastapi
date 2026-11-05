from fastapi import FastAPI
from fastapi.responses import JSONResponse


def register_error_handlers(app:FastAPI) -> None:
    @app.exception_handler(ValueError)
    async def _task_not_found(_: FastAPI, exc: ValueError) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})