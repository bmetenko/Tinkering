import rectpack as rp
import fastapi as fa
from pydantic import BaseModel


class Canvas(BaseModel):
    canvas_size: int


app = fa.FastAPI()


@app.get("/")
def root():
    return {"message": "Attempts at a square packing API based on rect pack, "
                       "specify a size for canvas using /assign/?canvas=5"}


@app.get("/create/{canvas_id}")
def create(canvas_id: int, canvas: Canvas):
    return {"item_id": canvas_id, **canvas.dict()}

