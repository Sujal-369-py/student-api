import os
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable is not set")

client = AsyncIOMotorClient(MONGO_URI)
db = client["test_subject_1"]["users"]

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

@app.get("/get-student")
async def student_details(student_id: int):
    result = await db.find_one({"id": student_id}, {"_id": 0})
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return result

@app.post("/add-student")
async def insert_student(user_data: User):
    user = user_data.dict()
    existing = await db.find_one({"id": user["id"]})
    if existing:
        raise HTTPException(status_code=409, detail="Student ID already exists")
    await db.insert_one(user)
    return {"message": "Student created successfully"}
@app.get("/test-mongo")
async def test_mongo():
    try:
        await db.find_one({})
        return {"status": "connected"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

