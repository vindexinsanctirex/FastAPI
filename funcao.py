from fastapi import HTTPException

def ler_item(item_id: int, items: list):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")