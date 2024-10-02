from typing import Annotated, List
from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def users_request(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get('/users/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='Message not found')

@app.post('/user/{username}/{age}')
async def put_user(username: Annotated[str, Path(min_length=3, max_length=30, description='Enter your Username', example='Bob')],
                   age: Annotated[int, Path(ge=1, le=100, description='Enter your age')]) -> User:
    if not users:
        new_user = User(id=1, username=username, age=age)
        users.append(new_user)
    else:
        new_id = users[-1].id + 1
        new_user = User(id=new_id, username=username, age=age)
        users.append(new_user)

    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, description='Write id to change')],
                      username: Annotated[str, Path(min_length=3, max_length=30, description='Enter your Username', example='Bob')],
                      age:  Annotated[int, Path(ge=1, le=100, description='Enter your age')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found ')


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, description='Write id to delete')]) -> User:
    for user in users:
        if user.id == user_id:
            delete_user = user
            users.remove(user)
            return delete_user
    raise HTTPException(status_code=404, detail='User was not found ')