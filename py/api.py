import rectpack as rp
import fastapi as fa
from pydantic import BaseModel


class Canvas(BaseModel):
    canvas_size: int


app = fa.FastAPI()


@app.get("/")
def root():
    return {"message": "Attempts at a square packing API based on rect pack."}


@app.post("/create/")
def create(canvas: Canvas):
    return canvas

