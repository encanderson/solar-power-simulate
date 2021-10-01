from fastapi import FastAPI
from app.config import settings
from starlette.middleware.cors import CORSMiddleware
from app.api import router

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url="/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

app.include_router(router)

# allow_origins=["*"]
