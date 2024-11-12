from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (altere conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados
class Item(BaseModel):
    name: str
    price: float

# Rota de teste
@app.get("/")
def read_root():
    return {"message": "opa eai"}

# Rota POST
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
