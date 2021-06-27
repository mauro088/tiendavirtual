import uvicorn
from app.application import createapp


app = createapp()

if __name__ == "__main__" :
    uvicorn.run(app)