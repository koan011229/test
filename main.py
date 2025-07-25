from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services import transcribe_youtube

app = FastAPI()
 
# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 특정 도메인만 허용하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 모델
class YoutubeRequest(BaseModel):
    url: str

@app.post("/transcribe")
def transcribe(request: YoutubeRequest):
    text = transcribe_youtube(request.url)
    return {"text": text}