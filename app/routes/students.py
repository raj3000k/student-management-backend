from fastapi import APIRouter, HTTPException
from typing import List, Optional
from app.db.mongodb import collection
from app.models.schemas import Student, StudentResponse
from bson import ObjectId

router = APIRouter()

# Helper function 
def student_helper(student: dict) -> dict:
    
    address = student.get("address", {})
    city = address.get("city", "")  # Default empty string 
    country = address.get("country", "")  # Default empty string
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": {
            "city": city,
            "country": country
        }
    }



# POST Creating a new Student
@router.post("/", response_model=StudentResponse)
async def create_student(student: Student):
    student_dict = student.dict()  
    result = collection.insert_one(student_dict)  
    new_student = collection.find_one({"_id": result.inserted_id}) 
    return student_helper(new_student) 


@router.get("/", response_model=List[StudentResponse])
async def list_students(country: Optional[str] = None, age: Optional[int] = None):
    
    filter_criteria = {}
    
    
    if country:
        filter_criteria['address.country'] = country
    
   
    if age is not None:  
        filter_criteria['age'] = {"$gte": age}

    
    students = collection.find(filter_criteria)
    
   
    return [student_helper(student) for student in students]


# Fetch a student by their id
@router.get("/{id}", response_model=StudentResponse)
async def fetch_student(id: str):
    student = collection.find_one({"_id": ObjectId(id)})  
    if student is None:  
        raise HTTPException(status_code=404, detail="Student not found")
    return student_helper(student)  

# Update student by their ID
@router.patch("/{id}", status_code=204)  
async def update_student(id: str, student: Student):
    updated_student = collection.find_one_and_update(
        {"_id": ObjectId(id)},  
        {"$set": student.dict()},  
        return_document=True  
    )
    if updated_student is None:  
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully"} 

#Delete student by their ID
@router.delete("/{id}", status_code=200) 
async def delete_student(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})  
    if result.deleted_count == 0:  
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}  
