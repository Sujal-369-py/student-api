from fastapi import FastAPI,Path

app = FastAPI() 

students = {
    1 : {
        "Name" : "John",
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
        "Name" : "Vanshika",
        "Age" : "21",
        "Course": "BCA-III",
        "Gender" : "Female"
    }
}

@app.get("/") 
def greet(): 
    return {"Hello" : "world"}

@app.get("/get-student/{student_id}") 
def get_student(student_id:int = Path(...,description="Enter the student id for student deatils",gt=0,le=3)): 
    return students[student_id]

@app.get("/get-student-by-name/{student_name}") 
def get_student(student_name : str):
    for student_id in students:  
        if students[student_id]["Name"] == student_name: 
            return students[student_id] 
    return {student_name: "Not found in records"}
        