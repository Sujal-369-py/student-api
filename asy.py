from fastapi import FastAPI 
import asyncio

app = FastAPI() 

@app.get("/async-demo") 
async def async_demo(): 
    await asyncio.sleep(5)
    return {"message":"finsihed async task!"}
