from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers.pages import pages
from app.controllers.api import users

def createapp():
    app = FastAPI(
        title = "tienda",
        # redoc_url="/redoc",
        # openapi_url="openapi.json"
    )
    app.mount("/public", StaticFiles(directory="public"), name="public")

    app.include_router(
        pages.router,
        tags=["pages"]
    )

    app.include_router(
        users.router,
        prefix="/users",
        tags=["users"]
    )

    return app


