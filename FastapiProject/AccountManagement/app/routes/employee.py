from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.employee import EmployeeCreate, EmployeeOut
from app.crud import employee as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=EmployeeOut)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)

@router.get("/", response_model=List[EmployeeOut])
def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@router.get("/{emp_id}", response_model=EmployeeOut)
def get_employee_by_id(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/{emp_id}", response_model=EmployeeOut)
def update_employee(emp_id: int, emp: EmployeeCreate, db: Session = Depends(get_db)):
    updated = crud.update_employee(db, emp_id, emp)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated

@router.delete("/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_employee(db, emp_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Deleted successfully"}
