from fastapi import FastAPI,Path
from pydantic import BaseModel 
from typing import Optional
import json
import os

app = FastAPI() 

# Load students from JSON if it exists
if os.path.exists("students.json"):
    with open("students.json", "r") as f:
        students = json.load(f)
else:
    students = {
        1: {"Name": "Aman", "Age": 21, "Dept": "Bca-III"},
        2: {"Name": "Raman", "Age": 20, "Dept": "Bca-III"}
    }

# Function to save current dictionary to JSON
def save_students():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)

class Student(BaseModel): 
    Name : str 
    Age : int
    Dept : str


@app.get("/Get-Student-By-Id/{student_id}") 
def get_stud(student_id : int = Path(...,description="Enter the student id for student deatils : ")):
    if student_id not in students: 
        return {"Error":f"student_id : {student_id} does not exit"} 
    return students[student_id]


@app.put("/Add-Student") 
def add_stud(student_id : int,new_stud : Student): 
    if student_id in students: 
        return {"Error":f"Student_id : {student_id} already exits."}
    #here what would be logic
    students[student_id] = new_stud.dict()
    save_students() 
    return students[student_id]
