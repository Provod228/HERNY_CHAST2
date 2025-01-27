from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
router = APIRouter(prefix='/project', tags=['Фронтенд'])

router.mount("/static", StaticFiles(directory="templates/static"), name="static")
templates = Jinja2Templates(directory='templates')
data = {'message': "message test", 'title': "title test"}


@router.get('/students', response_class=HTMLResponse)
async def get_students_html(request: Request):
    return templates.TemplateResponse(name='entrance_jornal.html', context={'request': request, 'data': data})


@router.get("/login")
async def login():
    return FileResponse("templates/login.html")


@router.get("/")
async def root():
    return FileResponse("templates/login.html")


@router.get("/registration")
async def registration():
    return FileResponse("templates/registration.html")

