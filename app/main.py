from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.chat import chat_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend"), name="static") # Підключення статичних файлів (frontend)

app.include_router(chat_router) # Підключення маршрутів

@app.get("/")
async def read_index():
    return FileResponse("../frontend/index.html")

if __name__ == "__main__": # Запуск сервера
    import uvicorn
    uvicorn.run(app)