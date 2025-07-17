from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 특정 도메인만 허용하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    value: int

@app.get("/")
def root():
    return {"message": "FastAPI 서버가 실행 중입니다!"}

@app.post("/square")
def square(input: Input):
    return {"result": input.value ** 2}

@app.get("/square/{value}")
def square_get(value: int):
    return {"result": value ** 2}
