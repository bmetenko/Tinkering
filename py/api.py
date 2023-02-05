from typing import List

import rectpack as rp
import fastapi as fa
from pydantic import BaseModel

class Rect(BaseModel):
    width: int
    height: int


class Canvas(BaseModel):
    canvas_size: int
    contents: List[Rect]


app = fa.FastAPI()


@app.get("/")
def root():
    return {"message": "Attempts at a square packing API based on rect pack."}


@app.post("/create/", status_code=fa.status.HTTP_201_CREATED)
def create(canvas: Canvas):
    return canvas

