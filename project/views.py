from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from registration_db import *
from starlette.requests import Request
from file_db.interlayer_db import *
from file_db.editing_db import hash_password


data_base = 'school.db'

app = FastAPI()
router = APIRouter(prefix='/project', tags=['Фронтенд'])

router.mount("/static", StaticFiles(directory="templates/static"), name="static")
templates = Jinja2Templates(directory='templates')


@router.get('/students', response_class=HTMLResponse)
async def get_students_html(request: Request):
    connection = sqlite3.connect(data_base)
    cursor = connection.cursor()
    data_test = Role.get(cursor_db=cursor)
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


@router.post("/login")
async def post_login(user: UserEntrance):
    connection = sqlite3.connect(data_base)
    cursor = connection.cursor()
    # role_user = Role.get(
    #     cursor_db=cursor,
    #     id=User.get(cursor_db=cursor, email=user.email, password=hash_password(user.password))[0]['role_id']
    # )[0]['title']
    # print(role_user)    # не трогать, это получение роли
    if User.get(cursor_db=cursor, email=user.email, password=hash_password(user.password)) != []:
        connection.commit()
        connection.close()
        print('f')
        return {"message": True}
    else:
        connection.close()
        print('fff')
        return {"message": False}


@router.get("/registration")
async def registration():
    return FileResponse("templates/registration.html")


@router.post("/registration")
async def post_registration(user: UserRegistration):
    connection = sqlite3.connect(data_base)
    cursor = connection.cursor()
    if (
            User.get(cursor_db=cursor, email=user.email) == [] and
            User.get(cursor_db=cursor, login=user.login) == []
    ):
        User.add(
            cursor_db=cursor,
            username=user.username,
            login=user.login,
            email=user.email,
            password=user.password_input,
        )
        connection.commit()
        connection.close()
        return {"message": True}
    else:
        connection.close()
        return {"message": False}

app.include_router(router)
