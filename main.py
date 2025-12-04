from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from funcao import ler_item

app = FastAPI()

items = []
next_id = 1

class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    valor: float = 0.0

class Item(ItemCreate):
    id: int

class ItemPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    valor: float | None = None

@app.post('/items', response_model=Item)
def create_item(item: ItemCreate):
    global next_id
    new_item = Item(id=next_id, **item.dict())
    items.append(new_item)
    next_id += 1
    return new_item

@app.get('/items')
def get_items():    
    return items

@app.get('/')
def listar_rotas():
    return {
        "items": "http://127.0.0.1:8000/items",
        "docs": "http://127.0.0.1:8000/docs"
    }

@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int):
    return ler_item(item_id)

@app.put('/items/{item_id}', response_model=Item)
def atualizar_item(item_id: int, dado: ItemCreate):
    for i in enumerate(items):
        if items.id == item_id:
            item_atualizado = Item(id=item_id, **dado.dict())
            items[i] = item_atualizado
            return item_atualizado
    raise HTTPException(status_code=404, detail="Item not found")

@app.patch('/items/{item_id}',response_model=Item)
def atualizar_produto(item_id:int,dado:ItemPatch):
    for i, item in enumerate(items):
        if item.id == item_id:
            item_atualizado = dado.dict(exclude_unset=True)
            for chave, valor in item_atualizado.items():
                setattr(item,chave,valor)

            items[i] = item
            return item
    raise HTTPException(404,'item não foi encontrado')