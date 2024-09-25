from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main Page"}

# get - адрес строки ?переменная=значение
# post - формы - оформить заказ в магазине
# put
# delete - удаление