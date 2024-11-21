import uvicorn
from fastapi import FastAPI


app = FastAPI()

app.include_router(router) #  Тут будет наш роутер для эндпоинтов

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
