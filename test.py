from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def my_func():
    return "My API is running"

@app.post("/data")
def my_post(data: TextInput): 
    explanation = f"Received text length: {len(data.text)} characters"
    return {
        "original_text": data.text,
        "ai_explanation": explanation
    }


