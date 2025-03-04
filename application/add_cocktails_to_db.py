import csv
from application.vector import setup_vector_db

def load_cocktails_dataset():
    cocktails = []
    with open("final_cocktails.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cocktails.append(row)
    return cocktails

def add_cocktails_to_db():
    cocktails = load_cocktails_dataset()
    dimension = 384
    metric = "cosine"
    index_name = "quickstart"

    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric=metric,
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    index, embeddings = setup_vector_db()

    texts = []
    metadatas = []
    for cocktail in cocktails:
        text = (
            f"Id: {cocktail['id']}, "
            f"Name: {cocktail['name']}, "
            f"Alcoholic: {cocktail['alcoholic']}, "
            f"Category: {cocktail['category']}, "
            f"Glass Type: {cocktail['glassType']}, "
            f"Ingredients: {cocktail['ingredients']}, "
            f"Instructions: {cocktail['instructions']}, "
            f"DrinkThumbnail: {cocktail['drinkThumbnail']}, "
            f"IngredientMeasures: {cocktail['ingredientMeasures']}, "
            f"Text: {cocktail['text']}, "
        )
        texts.append(text)

        metadata = {
            "id": cocktail["id"],
            "name": cocktail["name"],
            "alcoholic": cocktail["alcoholic"],
            "category": cocktail["category"],
            "glassType": cocktail["glassType"],
            "instructions": cocktail["instructions"],
            "drinkThumbnail": cocktail["drinkThumbnail"],
            "ingredients": cocktail["ingredients"],
            "ingredientMeasures": cocktail["ingredientMeasures"],
            "text": cocktail["text"]
        }
        metadatas.append(metadata)

    embeddings_list = embeddings.embed_documents(texts)

    vectors = []
    for i, (metadata, embedding) in enumerate(zip(metadatas, embeddings_list)):
        vectors.append({
            "id": metadata["id"],
            "values": embedding,
            "metadata": metadata
        })

    index.upsert(
        vectors=vectors,
        namespace="cocktails" 
    )

    print(index.describe_index_stats())

add_cocktails_to_db()