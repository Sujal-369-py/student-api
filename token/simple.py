from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

# Hardcoded username/password for simplicity
USERNAME = "admin"
PASSWORD = "password123"

@app.get("/secure-data")
def secure_data(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == USERNAME and credentials.password == PASSWORD:
        return {"message": "Welcome! You are authenticated."}
    raise HTTPException(status_code=401, detail="Unauthorized")
