import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.apis.api import api_router
from backend.core.config import settings


def create_application() -> FastAPI:
    """Create a FastAPI application with the appropriate settings.

    :returns: The configured FastAPI application.
    """
    application = FastAPI(title="Kennisfestival")
    application.include_router(api_router)
    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    return application


app = create_application()


def serve(host: str = "0.0.0.0", port: int = 5002, reload: bool = True) -> None:
    """Start uvicorn process for the FastAPI application.

    :param host: The host on which to expose the FastAPI application.
    :param port: The port to which to bind the webserver.
    :param reload: Should the application be reloaded on file changes.
    """
    uvicorn.run(
        "backend.main:app",
        host=host,
        port=port,
        reload=reload
    )
