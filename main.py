import uvicorn
from app.application import createapp
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = createapp()

if __name__ == "__main__" :
    uvicorn.run(app)