from fastapi import FastAPI
from app.api.routes import router
from app.api.error_handlers import register_error_handlers

app = FastAPI(title="TODO API", version="1.0.0")
app.include_router(router)
register_error_handlers(app)