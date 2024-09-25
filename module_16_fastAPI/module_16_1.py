from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def main_page() -> str:
    return "Главная страница"

@app.get('/user', response_class=PlainTextResponse)
async def users_check(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст {age}."

@app.get("/user/admin", response_class=PlainTextResponse)
async def admin_page() -> str:
    return "Вы вошли как администратор"

@app.get('/user/{user_id}', response_class=PlainTextResponse)
async def user_number(user_id: int) -> str:
    return f'Вы вошли как пользователь №{user_id}'






