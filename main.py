from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

app = FastAPI(title="Cinevoice AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI()


@app.get("/")
def home():
    return {
        "message": "Cinevoice AI Backend is Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


class TextRequest(BaseModel):
    text: str


@app.post("/generate")
def generate(request: TextRequest):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=request.text
    )

    return {
        "input": request.text,
        "response": response.output_text
    }
        