# from pydantic import BaseModel, EmailStr

# # Request body for creating/updating employee
# class EmployeeBase(BaseModel):
#     name: str
#     email: EmailStr
#     designation: str

# # Schema for creating
# class EmployeeCreate(EmployeeBase):
#     pass

# # Schema for response (includes ID)
# class EmployeeOut(EmployeeBase):
#     id: int

#     class Config:
#         orm_mode = True


from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    age: int
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        from_attributes = True  # ✅ Pydantic v2 replacement for orm_mode
