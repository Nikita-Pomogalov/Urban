from http.client import HTTPException
from typing import Annotated, List
from fastapi import FastAPI, Path, HTTPException
from fastapi.openapi.utils import status_code_ranges
from pydantic import BaseModel


app = FastAPI()



class User(BaseModel):
    id: int
    username: str
    age: int

users: List[User] = []


@app.get('/users')
async def get_users() -> List[User]:
    return users

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
