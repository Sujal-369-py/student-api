import json 
from fastapi import FastAPI,Path
from pydantic import BaseModel 
from typing import Optional

app = FastAPI() 

def load():
    with open("students.json","r") as f: 
        students = json.load(f) 
    return students

def save(stud): 
    with open("students.json","w") as f:
        json.dump(stud,f,indent=4) 
students = load() 


class Student(BaseModel): 
    Name : str
    Age : str
    Dept : str 
    Gender : str

class Update(BaseModel):  
    Name : Optional[str] 
    Age : Optional[str] 
    Dept : Optional[str] 
    Gender : Optional[str] 



@app.get("/Student-Details/{student_id}") 
def student_details(student_id : str = Path(...,description="Enter student id for student deatils")):
    if student_id not in students: 
        return {"Error":"Student does not exists"} 
    return students[student_id]


@app.put("/Add-Student/{Student_id}") 
def add_stud(student_id : str,new_stud : Student): 
    if student_id in students: 
        return {"Error":"Student Already exists"}
    students[student_id] = new_stud.dict()
    save(students) 
    return students[student_id] 


@app.patch("/Update-Student/{student_id}")
def update_student(student_id: str, updated: Update):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    for key, value in updated.dict(exclude_unset=True).items():
        students[student_id][key] = value

    save(students)
    return students[student_id]


@app.delete("/Delete-student/{student_id}") 
def delete_stud(student_id : str): 
    if student_id not in students: 
        return {"Error":"Student does not exists"}
    del students[student_id] 
    save(students) 
    return {"Student deleted succesfully."} 




