#from fastapi import FastAPI, Body
#from typing import List
#from pydantic import BaseModel,Field

#app=FastAPI()

#class stud(BaseModel):
 #   id: int
#    name: str | None = Field(None,min_length=3,max_length=10)
 #   subjects: List[str] = []

#@app.post("/Student")
#async def stud_detail(Student:stud):
 #   return Student


from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Dict

app = FastAPI()

class Stud(BaseModel):
    id: int
    name: str | None = Field(None, min_length=3, max_length=10)
    subjects: List[str] = Field(default_factory=list)

# ✅ temporary database
students_db: Dict[int, Stud] = {}

# ✅ POST – create student
@app.post("/student")
async def create_student(student: Stud):
    students_db[student.id] = student
    return student

# ✅ GET – fetch student by id
@app.get("/student/{student_id}")
async def get_student(student_id: int):
    return students_db.get(student_id, {"error": "Student not found"})
