from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.llm import get_answer, find_cocktails_by_ingredients

chat_router = APIRouter()

class ChatRequest(BaseModel): # Модель для запитів
    question: str

@chat_router.post("/chat") # Ендпоінт для чату
async def chat(request: ChatRequest):
    try:
        if "favourite ingredients" in request.question.lower():
            ingredients = request.question.lower().replace("favourite ingredients", "").strip().split(",")
            response = find_cocktails_by_ingredients(ingredients)
        else:
            response = get_answer(request.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))