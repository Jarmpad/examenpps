from fastapi import FastAPI
from app.routers import tasks
from app.database import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(tasks.router)


app.include_router(tasks.router)


# Código que se añade
@app.get("/version")
def version():
    return {"message": "Armario Padilla, Juan Antonio - v0"}
