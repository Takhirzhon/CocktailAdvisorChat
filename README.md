# Cocktail Chat

This application allows you to search for cocktails, save favorite ingredients, and receive recommendations. The project implements a chatbot for cocktail recommendations using RAG (Retrieval-Augmented Generation). The bot integrates with Pinecone for storing vector embeddings of cocktails and uses the Together API for generating responses.

## Requirements
To work with the project, you need:
1. Python 3.9 or a newer version.
2. API keys for Pinecone and Together API.
3. Libraries listed in requirements.txt.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cocktail-chatbot-rag.git
   cd cocktail-chatbot-rag
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your API keys:
   ```bash
   PINECONE_API_KEY=your_pinecone_api_key
   TOGETHER_API_KEY=your_together_api_key
   ```
4. Run the project:
   ```bash
   python main.py
   ```
   or
   ```bash
   uvicorn app.main:app --reload
   ```
   After that, open your browser.
   Main page: http://127.0.0.1:8000
   API documentation: http://127.0.0.1:8000/docs