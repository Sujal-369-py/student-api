from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pathlib import Path

app = FastAPI()

# MongoDB client
client = AsyncIOMotorClient(
    "mongodb+srv://UserXts_db_user:6UOSD2hon4O9dnz5@cluster0.znfwoni.mongodb.net/school?retryWrites=true&w=majority"
)
db = client["school"]["stud"]

# Path to the HTML file
HTML_FILE = Path(__file__).parent / "ts-3.html"
success = Path(__file__).parent / "success.html"

# Serve the HTML file
@app.get("/", response_class=FileResponse)
async def get_form():
    return HTML_FILE

# Handle form submission
@app.post("/user")
async def add_user(first_name: str = Form(...), last_name: str = Form(...)):
    user_dict = {"first_name": first_name, "last_name": last_name}
    result = await db.insert_one(user_dict)
    return FileResponse(success)
