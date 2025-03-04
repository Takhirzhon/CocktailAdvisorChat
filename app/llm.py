import os
from langchain_together import Together
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from app.vector_db import setup_vector_db

from dotenv import load_dotenv
load_dotenv()

llm = Together( # Ініціалізація Together LLM
    model='meta-llama/Llama-3.3-70B-Instruct-Turbo',
    together_api_key=os.getenv("TOGETHER_API_KEY"),
    temperature=0.7,
    max_tokens=512
)

index, embeddings = setup_vector_db() # Ініціалізація RAG

vector_store = PineconeVectorStore(index, embeddings, "text")
retriever = vector_store.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

def get_answer(question): # Функція для отримання відповіді
    return qa.run(question)

def find_cocktails_by_ingredients(ingredients): # Функція для пошуку коктейлів за інгредієнтами
    query = f"Find cocktails with {', '.join(ingredients)}"
    return qa.run(query)