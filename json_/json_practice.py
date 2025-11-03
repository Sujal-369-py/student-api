import json

students = {
    1: {"Name": "Aman", "Age": 21, "Dept": "BCA-III", "Gender": "Male"},
    2: {"Name": "Raman", "Age": 20, "Dept": "BCA-III", "Gender": "Male"},
    3: {"Name": "Shweta", "Age": 22, "Dept": "BCA-III", "Gender": "Female"},
    4: {"Name": "Vikram", "Age": 23, "Dept": "BCA-III", "Gender": "Male"}
}

# Write to JSON file
with open("json_/students.json", "a") as f:
    json.dump(students, f, indent=4)

# with open("json_/students.json","r") as f: 
#     temp = json.load(f) 

# print(temp)
