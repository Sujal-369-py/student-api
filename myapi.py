from fastapi import FastAPI,Path
from typing import Optional 
from pydantic import BaseModel

app = FastAPI() 

student = {
    1 : {
        "Name" : "Hanish",
        "Age" : "19",
        "Course": "BCA-III",
        "Gender" : "Male"
    },
    2 : {
        "Name" : "Ayush",
        "Age" : "20",
        "Course": "BCA-III",
        "Gender" : "Male"
    },
    3 : {
        "Name" : "Shweta",
        "Age" : "21",
        "Course": "BCA-III",
        "Gender" : "Female"
    }
}

@app.get("/") 
def greet(): 
    return {"Name" : "Your data"}


#Path 
#get: it is used to see the data
@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(...,description="Enter the student id for student details.",gt=0)): 
    return student[student_id]

#Query
@app.get("/get-by-name/{student_id}") 
def get_student(*,student_id : int,name: Optional[str] = None,test: int): 
    for student_id in student: 
        if student[student_id]["Name"] == name: 
            return student[student_id] 
    return {name : "Not found"}

class Student(BaseModel): 
    Name : str 
    Age : str
    Course: str 
    Gender: str


#Post method : it is used to add data
@app.post("/Create-new-student/{student_id}")
def creat_stud(student_id : int,new_student:Student): 
    if student_id in student: 
        return {"Error":f"Student_id {student_id} already exist."}
    student[student_id] = new_student
    return student[student_id]

class UpdateStudent(BaseModel): 
    Name : Optional[str] = None
    Age : Optional[str] = None
    Course : Optional[str] = None
    Gender : Optional[str] = None

#put : it is used to update the  existing data
@app.put("/Update-data/{student_id}") 
def update_data(student_id: int, new_data: UpdateStudent): 
    if student_id not in student: 
        return {"Error": f"student_id {student_id} does not exist"} 
    
    if new_data.Name is not None: 
        student[student_id]["Name"] = new_data.Name
    if new_data.Age is not None: 
        student[student_id]["Age"] = new_data.Age
    if new_data.Course is not None: 
        student[student_id]["Course"] = new_data.Course
    if new_data.Gender is not None: 
        student[student_id]["Gender"] = new_data.Gender
    
    return student[student_id]

#Delete : it is used to delete data
@app.delete("/Delete-Student/{student_id}") 
def delete_stud(student_id:int): 
    if student_id not in student: 
        return {"Error":"Student does not found"} 
    del student[student_id] 
    return {"Message":"Student deleted succesfully"}

