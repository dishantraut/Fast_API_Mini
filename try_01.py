from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.get("/home")
async def HW():
    return {"Hello": "World"}

# Path Parameter [http://127.0.0.1:8000/comp/12]
@app.get('/comp/{comp_id}') 
async def get_comp(comp_id : int):
    return {'Component ID':comp_id}

# Query Parameter [http://127.0.0.1:8000/comp/?num1=12&text=RST Forum]
@app.get('/comp/')
async def read_comp(num1 : int, text : str):
    return {'Number':num1, 'Text':text}

# [http://127.0.0.1:8000/items/12?q=demo]
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
