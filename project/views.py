from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse


app = FastAPI()


app.mount("/static", StaticFiles(directory="WEB/static"), name="static")


@app.get("/login")
def root():
    return FileResponse("WEB/login.html")


@app.get("/")
def root():
    return FileResponse("WEB/login.html")


@app.get("/regestartion")
def root():
    return FileResponse("WEB/regestartion_jornal.html")
