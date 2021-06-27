from fastapi.responses import RedirectResponse
from fastapi.routing import APIRouter
from fastapi import Form
from fastapi import Request, Response
from ...models.users import Users
from ...models.db import session
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def index():
    return RedirectResponse("/public/index.html")

@router.post("/register")
async def register(request: Request, email: str = Form(...), password: str = Form(...), name: str = Form(...)):
    user = Users(email=email, password=password, name=name)
    try:
        session.add(user)
        session.commit()
        template_params = {
            "request": request,
            "name" : name
        }
        return templates.TemplateResponse("registerok.html", template_params)
    except:
        return templates.TemplateResponse("registerok.html", template_params)
    return templates.TemplateResponse("registerok.html", template_params)


@router.post("/login")
async def register(request: Request, email: str = Form(...), password: str = Form(...)):
    user = session.query(Users).filter(Users.email == email)
    try:
        #Hacer operacione de login comparar password, etc
        return templates.TemplateResponse("loginok.html", template_params)
    except:
        return templates.TemplateResponse("registerok.html", template_params)
    return templates.TemplateResponse("registerok.html", template_params)
