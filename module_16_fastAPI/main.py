from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

@app.get("/user/A/B")
async def news() -> dict:
    return {"message": f"Hello, Tester"}

@app.get('/id')
async def id_paginator(username: str = 'alex', age: int = 24) -> dict:
    return {'User': username, 'Age': age}

@app.get("/user/{username}/{id}")
async def news(username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username', example='montes')],
               id: int) -> dict:
    return {"message": f"Hello, {username} {id}"}





# get - адрес строки ?переменная=значение
# post - формы - оформить заказ в магазине
# put
# delete - удаление