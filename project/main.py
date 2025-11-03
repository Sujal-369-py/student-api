from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

# Paths relative to current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Serve static file (CSS)
app.mount("/static", StaticFiles(directory=current_dir), name="static")

# Templates (HTML)
templates = Jinja2Templates(directory=current_dir)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["school"]["stud"]

class Student(BaseModel):
    Age: Optional[int]
    Gpa: Optional[float]

class Update(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gpa: Optional[float] = None

# Serve frontend
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# CRUD APIs
@app.get("/students/{student_name}")
def get_student(student_name: str):
    student = db.find_one({"name": student_name}, {"_id": 0})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_name}")
def add_student(student_name: str, new_stud: Student):
    if db.find_one({"name": student_name}):
        raise HTTPException(status_code=400, detail="Student already exists")
    db.insert_one({"name": student_name, **new_stud.dict()})
    return {"message": "Student inserted successfully"}

@app.patch("/students/{student_name}")
def update_student(student_name: str, updated_data: Update):
    if not db.find_one({"name": student_name}):
        raise HTTPException(status_code=404, detail="Student not found")
    db.update_one(
        {"name": student_name},
        {"$set": {k: v for k, v in updated_data.dict().items() if v is not None}}
    )
    new_name = updated_data.name if updated_data.name else student_name
    updated_student = db.find_one({"name": new_name}, {"_id": 0})
    return updated_student

@app.delete("/students/{student_name}")
def delete_student(student_name: str):
    if not db.find_one({"name": student_name}):
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete_one({"name": student_name})
    return {"message": "Student deleted successfully"}
