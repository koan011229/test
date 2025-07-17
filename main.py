from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    value: int

@app.post("/square")
def square(input: Input):
    return {"result": input.value ** 2}
