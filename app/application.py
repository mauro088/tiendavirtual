from fastapi import FastAPI


def createapp():
    app = FastAPI(
        title = "tienda",
        redoc_url="/redoc",
        openapi_url="openapi.jason"

    )
    return app



