from fastapi import FastAPI,HTTPException 
from pydantic import BaseModel 
from jose import jwt,JWTError,ExpiredSignatureError
from datetime import datetime,timedelta 
import secrets 
from passlib.context import CryptContext
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI() 
client = AsyncIOMotorClient(
    "mongodb+srv://UserXts_db_user:6UOSD2hon4O9dnz5@cluster0.znfwoni.mongodb.net/",
    tls=True,
    tlsAllowInvalidCertificates=False
)
db = client["test_subject_1"]["test_subject_data"] 
SECREAT_KEY = secrets.token_hex(64) 
ALGORITHM = "HS256" 

pwt_context = CryptContext(schemes=['bcrypt'],deprecated="auto")
def hash_password(plain_pass : str): 
    return pwt_context.hash(plain_pass)

def create_token(data:dict): 
    to_encode = data 
    expire = datetime.utcnow()+timedelta(minutes=1) 
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECREAT_KEY,algorithm=ALGORITHM)

class UserDetails(BaseModel): 
    username : str 
    password : str 
    age : int 
    gender : str 

@app.post("/Register-user") 
async def register_user(user : UserDetails): 
    user_data = user.dict()
    password = user_data["password"]
    user_data["password"] = hash_password(password)
    await db.insert_one(user_data)
    return {"message":"Registered successfully."}


@app.get("/get-token") 
async def get_token(user_name : str,user_pass : str): 
    user_data = await db.find_one({"username":user_name})
    if not user_data: 
        raise HTTPException(status_code=404,detail="User not found.") 

    if not pwt_context.verify(user_pass,user_data["password"]):
        raise HTTPException(status_code=401,detail="Wrong password")

    token_data = {"username":user_data["username"]}
    token = create_token(token_data)
    return {"Message":f"Your token is : {token}"} 

@app.get("/Login") 
def login(token:str): 
    try: 
        token_details = jwt.decode(token,SECREAT_KEY,algorithms=[ALGORITHM]) 
        return {"Message":"Login success."} 
    except ExpiredSignatureError: 
        raise HTTPException(status_code=401,detail="Token has expired.")
    except JWTError: 
        raise HTTPException(status_code=401,detail="Unauthorised acces.")



