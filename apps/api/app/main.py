from fastapi import FastAPI,APIRouter
import uvicorn
from pydantic import BaseModel
from app.config import db
from fastapi.middleware.cors import CORSMiddleware
from app.config import db

origins= [
    "http://localhost:3000"
]

def init_app():
    db.init()

    app = FastAPI(
        title= "Tast management",
        description= "A task management app",
        version= "0.1.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.on_event("startup")
    async def starup():
        await db.create_all()
    
    @app.on_event("shutdown")
    async def shutdown():
        await db.close()
   
    return app

app = init_app()

@app.get('/')
def root():
      return {"message": "Welcome to the Task Management API"}

def start():
    """ Alhumdullilah, Launched with 'poetry run start' at root level """
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)