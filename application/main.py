from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from application.chat import chat_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="../front"), name="static")

app.include_router(chat_router)

@app.get("/")
async def read_index():
    return FileResponse("../front/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)