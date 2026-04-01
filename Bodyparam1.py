from fastapi import FastAPI, Body
from typing import List
from pydantic import BaseModel,Field

app=FastAPI()

class stud(BaseModel):
    id: int
    name: str | None = Field(None,min_length=3,max_length=10)
    subjects: List[str] = []

@app.post("/Student")
async def stud_detail(Student:stud):
    return Student