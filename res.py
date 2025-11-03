from fastapi import FastAPI, HTTPException

app = FastAPI()

students = ["Alice", "Bob"]

# 200 OK (default, no need to write)
@app.get("/students", status_code=200)
def all_students():
    return {"students": students}

# 201 Created
@app.post("/students", status_code=201)
def add_student(name: str):
    students.append(name)
    return {"message": f"{name} added!"}

# 404 Not Found handled with HTTPException
@app.get("/students/{name}", status_code=200)
def get_student(name: str):
    if name not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student": name}

# 202 Accepted
@app.put("/students/{name}", status_code=202)
def update_student(name: str, new_name: str):
    if name not in students: 
        raise HTTPException(status_code=404,detail="Student odes not found") 
    return {"message":f"{name} will be update to {new_name}"}

