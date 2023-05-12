from trans import do_trans

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

@app.post("/trans")
def trans(input: str = None):
    return JSONResponse(content=json.loads(do_trans(input)))