import uvicorn
import os
from dotenv import load_dotenv
from agent import chatbot
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

 
load_dotenv()

origins_str = os.getenv("CORS_ORIGINS", "")

if origins_str:
    origins = [origin.strip().rstrip("/") for origin in origins_str.split(",") if origin.strip()]
else:
    origins = ["http://127.0.0.1:5500"]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chat")
def get_chat(prompt: str):
    if not prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is required")
    return {"response": chatbot(f"{prompt}")}

