from pydantic import BaseModel
from typing import Dict


class Address(BaseModel):
    city: str
    country: str


class Student(BaseModel):
    name: str
    age: int
    address: Address  

class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    address: Address 
