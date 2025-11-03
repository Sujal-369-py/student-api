import streamlit as st
import requests

st.title("Student Management System")

# ---------------- Fetch & Delete Section ----------------
student_id = st.text_input("Enter Student ID:")

if st.button("Fetch Details"):
    if student_id:
        response = requests.get(f"http://127.0.0.1:8000/Student-Details/{student_id}")
        if response.status_code == 200:
            data = response.json()
            st.info("Student Details:")
            st.json(data)
        else:
            st.error(response.json().get("Error", "Something went wrong"))

if st.button("Delete Student"):
    if student_id:
        response = requests.delete(f"http://127.0.0.1:8000/Delete-student/{student_id}")
        data = response.json()
        if response.status_code == 200:
            if "Student deleted succesfully." in data:
                st.success(data["Student deleted succesfully."])
            else:
                st.error(data.get("Error", "Something went wrong"))
        else:
            st.error(data.get("Error", "Something went wrong"))

# ---------------- Add New Student Section ----------------
if st.button("Add New Student"):
    # Show inputs inside an expander for neat UI
    with st.expander("Enter New Student Details"):
        new_id = st.text_input("Student ID", key="new_id")
        new_name = st.text_input("Name", key="new_name")
        new_age = st.text_input("Age", key="new_age")
        new_dept = st.text_input("Dept", key="new_dept")
        new_gender = st.text_input("Gender", key="new_gender")

        if st.button("Submit New Student"):
            if new_id and new_name and new_age and new_dept and new_gender:
                new_student = {
                    "Name": new_name,
                    "Age": new_age,
                    "Dept": new_dept,
                    "Gender": new_gender
                }
                response = requests.put(f"http://127.0.0.1:8000/Add-Student/{new_id}", json=new_student)
                data = response.json()
                if response.status_code == 200:
                    st.success(f"Student {new_id} added successfully!")
                    st.json(data)
                else:
                    st.error(data.get("Error", "Something went wrong"))
            else:
                st.warning("Please fill in all fields!")
