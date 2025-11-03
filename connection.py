from pymongo import MongoClient 

client = MongoClient("mongodb://localhost:27017/") 
data_base = client["school"] 
db = data_base["stud"] 

# name = input("Enter the name : ") 
# age = int(input("Enter the age : ")) 
# gpa = float(input("Enter the gpa : "))

# res = db.insert_one({"name":name,"age":age,"gpa":gpa}) 
# if res.acknowledged: 
#     print(f"Student added successfully") 
# else: 
#     print("CAn not add student")

# res = db.delete_many({"name":"Hanish"})
# if res.acknowledged: 
#     print(f"Student deleted successfully") 
# else: 
#     print("Can not delete student")

# db.insert_one({"name":"hanish","age":19,"gpa":6.8})
# db.insert_many([{"name":"yaman","age":20,"gpa":6.3},{"name":"ishita","age":21,"gpa":7.4},{"name":"prerana","age":22,"gpa":8.2}])

# print(list(db.find({"name":"yaman"}))) 

# data = db.find({"name":"yaman"}) 

# for val in data: 
#     print(val)

# for doc in db.find({"gpa":{"$gt":7},},{"_id":0}): 
#     print(doc)

# data_base.create_collection("student")



