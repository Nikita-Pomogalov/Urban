from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Name: Example, age: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def put_user(username: Annotated[str, Path(min_length=3, max_length=30, description='Enter your Username', example='Bob')],
                   age: Annotated[int, Path(ge=1, le=100, description='Enter your age')]) -> str:
    new_index = str(int(max(users, key=int)) + 1)
    users[new_index] = f'Имя: {username}, возраст: {age}'
    return f'User {new_index} was registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(max_length=10, description='Write id to change')],
                      username: Annotated[str, Path(min_length=3, max_length=30, description='Enter your Username', example='Bob')],
                      age:  Annotated[int, Path(ge=1, le=100, description='Enter your age')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} has been updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(max_length=20, description='Write id to delete')]) -> str:
    users.pop(user_id)
    return f'The user {user_id} has been deleted'