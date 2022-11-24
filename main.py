import os
from fastapi import FastAPI, Request, Response
from endpoints.api.v1.create_session.endpoint.create_session import router as create_session_router

App = FastAPI(redoc_url=None, docs_url=None)
App.include_router(create_session_router, prefix='/api/v1/create_session')


@App.get('/')
def ping():
    return {"message": "pong"}
