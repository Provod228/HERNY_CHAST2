from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from registration_db import UserRegistration
from starlette.requests import Request
import sqlite3
from file_db import interlayer_db as editing

app = FastAPI()
router = APIRouter(prefix='/project', tags=['Фронтенд'])

router.mount("/static", StaticFiles(directory="templates/static"), name="static")
templates = Jinja2Templates(directory='templates')


@router.get('/students', response_class=HTMLResponse)
async def get_students_html(request: Request):
    connection = sqlite3.connect('school.db')
    cursor = connection.cursor()
    data_test = editing.Role.get(cursor_db=cursor)
    connection.commit()
    connection.close()
    return templates.TemplateResponse(
        name='entrance_jornal.html',
        context={
            'request': request,
            'data_test': data_test,
        }
    )


@router.get("/login")
async def get_login():
    return FileResponse("templates/login.html")


@router.post("/registration")
async def post_registration(user: UserRegistration):
    connection = sqlite3.connect('school.db')
    cursor = connection.cursor()
    if (
            editing.User.get(cursor_db=cursor, email=user.email) == [] and
            editing.User.get(cursor_db=cursor, login=user.login) == []
    ):
        # User.add(
        #     cursor_db=cursor,
        #     username=user.username,
        #     login=user.login,
        #     email=user.email,
        #     password=user.password_input,
        # )
        print('f')
        return {"message": "Registration successful"}
    else:
        print('fff')
        return {"message": "No registration successful"}


@app.get("/")
async def root():
    return FileResponse("access_true/login.html")


@router.get("/registration")
async def registration():
    return FileResponse("templates/registration.html")

app.include_router(router)