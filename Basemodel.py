from typing import List
from pydantic import BaseModel, Field

class Student(BaseModel):
   id: int
   name :str
   subjects: List[str] = []
   Fullname: str | None = Field(None, max_length=10)
   
data = {
   'id': 1,
   'name': 'Syed',
   'subjects': ["Eng", "Maths", "Sci"],
   'Fullname' : "Syedumar"
}

s1=Student(**data)
print(s1) #returns output
print(s1.model_dump()) #returns JSON output