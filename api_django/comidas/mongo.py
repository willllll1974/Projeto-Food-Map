from pymongo import MongoClient
from urllib.parse import quote_plus

usuario = "admin"
senha = quote_plus("Formig@tomica15032001")

client = MongoClient(
    f"mongodb://{usuario}:{senha}@localhost:27017/?authSource=admin"
)

db = client["ProjetoFaculdade"]

comidas_collection = db["comidas"]
