from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi import Form
from ...models.users import Users
from ...models.db import session

router = APIRouter()

@router.get("/")
async def list_users():
    result = session.query(Users).all()
    return result

@router.post("/")
async def create_user(email: str = Form(...), password: str = Form(...), name: str = Form(...)):
    user = Users(email=email, password=password, name=name)
    try:
        session.add(user)
        session.commit()
        result = JSONResponse({"message": "usuario creado"}, 201)
    except:
        result = JSONResponse({"message": "error"}, 406)
    return result

@router.get("/{user_id}")
async def read_user(user_id):
    user = session.query(Users).get(user_id)
    return user or JSONResponse({"message": "not found"}, 404)

@router.put("/{user_id}")
async def update_user(user_id):
    return {}

@router.delete("/{user_id}")
async def delete_user(user_id):
    user = session.query(Users).get(user_id)
    try:
        session.delete(user)
        session.commit()
        result = JSONResponse({"message": "deleted"}, 200)
    except:
        result = JSONResponse({"message": "not found"}, 404)
    return result


