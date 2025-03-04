import os
import time
from pinecone import Pinecone, ServerlessSpec
from langchain_community.embeddings import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

def setup_vector_db():
    index_name = "quickstart"
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    index = pc.Index(index_name)
    return index, embeddings