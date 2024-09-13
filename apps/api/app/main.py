"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""
import uvicorn
from contextlib import asynccontextmanager

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import AsyncGenerator


# Loguru
from .core.logger import logger


# Routers depends
# from api.routers.auth.router import router as router_auth
# from api.routers.blog.router import router as router_blog
# from api.routers.custom.router import router as router_custom
# from api.routers.artist.router import router as router_artist
# from api.routers.tasks.router import router as router_tasks


# Startup events
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator: 
     # FastAPI
    try:
        logger.info('❕FastAPI успешно запущен.')
    except Exception as e:
        logger.error(f'❌ FastAPI ошибка: {e}')

    yield



# endregion -------------------------------------------------------------------------


# region ---------------------------- APPLICATION -----------------------------------
app = FastAPI(
    lifespan=lifespan,
    title='Task Management ',
    # docs_url=None,
    # openapi_url=None,
    redoc_url=None,
)



# Routers
# app.include_router(router_auth)
# app.include_router(router_blog)
# app.include_router(router_custom)
# app.include_router(router_artist)
# app.include_router(router_tasks)



# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:8080',  # Next.js local port
        #'http://localhost', Будущий VDS ip
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Authorization',
    ],
)

def start():
    """ Alhumdullilah, Launched with 'poetry run start' at root level """
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)
