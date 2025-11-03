from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import certifi

client = AsyncIOMotorClient(
    "mongodb+srv://UserXts_db_user:6UOSD2hon4O9dnz5@cluster0.znfwoni.mongodb.net/school?retryWrites=true&w=majority",  # forces Python to use updated CA certs
)

db = client["school"]
collection = db["stud"]

async def main():
    result = await collection.insert_one({"name":"hanish","age":21,"gender":"male"})
    print("Inserted ID:", result.inserted_id)

    doc = await collection.find_one({"name": "hanish"})
    print("Fetched document:", doc)

asyncio.run(main())
