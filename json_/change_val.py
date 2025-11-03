import json

with open("json_/stud.json","r") as f:
    data = json.load(f) 

student_id = "2"

if student_id not in data: 
    print(f"Student_if {student_id} does not exist.") 
else: 
    del data[student_id] 
    print("Deleetd successfully") 

with open("json_/stud.json","w") as f: 
    json.dump(data,f,indent=4)
