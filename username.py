from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
import logging

# ---------- Setup ---------- #
app = FastAPI()
logging.basicConfig(level=logging.INFO)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
dataBase = client["user"]
db = dataBase["info"]

# Ensure username is unique
db.create_index("username", unique=True)

# ---------- Models ---------- #
class User(BaseModel):
    username: str
    password: str

# ---------- Hash Function ---------- #
def hashed(password: str) -> str:
    """
    Fun hash: adds '*$', '$*' around each character and shifts ASCII by 1000
    """
    new_pass = []
    for i in password:
        new_pass.append("*$")
        new_pass.append(str(ord(i) + 1000))
        new_pass.append("$*")
    return "".join(new_pass)

# ---------- Routes ---------- #

@app.post("/Sign-up")
def sign_up(user: User):
    # Check if username exists
    if db.find_one({"username": user.username}):
        raise HTTPException(status_code=409, detail="Username already exists.")

    # Insert user with hashed password
    db.insert_one({"username": user.username, "password": hashed(user.password)})
    logging.info(f"New user signed up: {user.username}")
    return {"status": "success", "message": "Account created successfully"}

@app.post("/Sign-in")
def sign_in(user: User):
    res = db.find_one({"username": user.username})
    
    if not res or res["password"] != hashed(user.password):
        raise HTTPException(status_code=400, detail="Username or password is wrong.")

    logging.info(f"User signed in: {user.username}")
    return {"status": "success", "message": f"Sign in successful, welcome {user.username}"}
