from fastapi import FastAPI,HTTPException
from pymongo import MongoClient
from typing import Optional 
from pydantic import BaseModel

app = FastAPI() 
class Student(BaseModel):  
    Age: Optional[int] 
    Gpa : Optional[float]


def get_db(): 
    client = MongoClient("mongodb://localhost:27017/")
    db = client["school"]["stud"] 
    return db
db = get_db()


@app.get("/find-student-by-name{student_name}") 
def find_student(student_name:str): 
    res = list(db.find({"name":student_name},{"_id":0})) 
    if res: 
        return res 
    raise HTTPException(status_code=404,detail="Student not found in record")


@app.put("/Add-students/{student_name}") 
def add_student(student_name:str,new_stud:Student): 
    res = list(db.find({"name":student_name})) 
    if res: 
        raise HTTPException(status_code=400,detail="Student already exists.")
    db.insert_one({"name":student_name,**new_stud.dict()}) 
    return {"Message":"Student inserted successfully."}

@app.delete("/Delete-stude/{student_name}") 
def delete_student(student_name:str): 
    res = list(db.find({"name":student_name})) 
    if not res: 
        raise HTTPException(status_code=404,detail="Student not found") 
    db.delete_one({"name":student_name}) 
    return {"Message":"Student deletd successfuly"} 
 
class Update(BaseModel): 
    name: Optional[str] = None
    age: Optional[int] = None 
    gpa : Optional[float] = None
@app.patch("/Update-student/{student_name}") 
def update_student(student_name:str,updated_data:Update): 
    res = list(db.find({"name":student_name})) 
    if not res: 
        raise HTTPException(status_code=404,detail="Student not found") 
    db.update_one(
        {"name": student_name},
        {"$set": {k: v for k, v in updated_data.dict().items() if v is not None}}
    )
    new_name = updated_data.name if updated_data.name else student_name
    updated_student = db.find_one({"name": new_name}, {"_id": 0})
    return updated_student
