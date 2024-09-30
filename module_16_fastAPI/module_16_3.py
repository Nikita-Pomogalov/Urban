from fastapi import FastAPI, Path
from typing import Annotated

from fastapi.responses import PlainTextResponse

app = FastAPI()

users = {'1': 'Name: Example, age: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def put_user(username: str, age: int) -> str:
    new_index = str(int(max(users, key=int)) + 1)
    users[new_index] = f'Имя: {username}, возраст: {age}'
    return f'User {new_index} was registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} has been updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'The user {user_id} has been deleted'