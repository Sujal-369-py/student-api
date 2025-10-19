from fastapi import FastAPI,HTTPException 
from motor.motor_asyncio import AsyncIOMotorClient 
import asyncio
from pydantic import BaseModel

client = AsyncIOMotorClient("mongodb+srv://UserXts_db_user:6UOSD2hon4O9dnz5@cluster0.znfwoni.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["test_subject_1"]["users"] 
app = FastAPI() 

class Users(BaseModel): 
    id : int 
    name : str 
    age : int 

@app.get("/get-student")
async def student_deatils(student_id : int): 
    result = await db.find_one({"id":student_id},{"_id":0}) 
    if not result: 
        raise HTTPException(status_code=404,detail="Student not found") 
    
    return result
@app.post("/add-student")
async def insert_student(user_data:Users):
    user = user_data.dict()
    result = await db.find_one({"id":user["id"]}) 
    if result: 
        raise HTTPException(status_code=402,detail="student id already exit")
    await db.insert_one(user) 
    return {"Message":"created student succesfully"} 
