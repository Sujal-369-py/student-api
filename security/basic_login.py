from fastapi import FastAPI,HTTPException 
from pydantic import BaseModel
from passlib.context import CryptContext 
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

pwt_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
client = AsyncIOMotorClient("mongodb://localhost:27017/") 
data_base = client["user"] 
db = data_base["info"] 

class User(BaseModel): 
    username:str 
    email:str
    password:str 
    age:int

def hashed(plain): 
    return pwt_context.hash(plain)

@app.put("/Create account")
async def create_account(user_details:User): 
    user = await db.find_one({"username":user_details.username}) 
    if user: 
        raise HTTPException(status_code=409,detail="Username already exits.")
    
    hashed_password = hashed(user_details.password) 
    user_data = user_details.dict() 
    user_data["password"] = hashed_password 
    await db.insert_one(user_data)
    return {"message":"user created succesfully."}

@app.get("/Login") 
async def login(username:str,password:str): 
    user = await db.find_one({"username":username})
    if not user or not pwt_context.verify(password,user["password"]): 
        raise HTTPException(status_code=404,detail="User does not exit.")
    return {"message":"Login success"}
    
