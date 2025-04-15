# from sqlalchemy.orm import Session
# from app import models, schemas

# # Create employee
# def create_employee(db: Session, employee: schemas.EmployeeCreate):
#     db_employee = models.employee.Employee(**employee.dict())
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee

# # Get all employees
# def get_employees(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.employee.Employee).offset(skip).limit(limit).all()

# # Get one employee by ID
# def get_employee(db: Session, employee_id: int):
#     return db.query(models.employee.Employee).filter(models.employee.Employee.id == employee_id).first()

# # Update employee
# def update_employee(db: Session, employee_id: int, updated_data: schemas.EmployeeCreate):
#     employee = db.query(models.employee.Employee).filter(models.employee.Employee.id == employee_id).first()
#     if employee:
#         for key, value in updated_data.dict().items():
#             setattr(employee, key, value)
#         db.commit()
#         db.refresh(employee)
#     return employee

# # Delete employee
# def delete_employee(db: Session, employee_id: int):
#     employee = db.query(models.employee.Employee).filter(models.employee.Employee.id == employee_id).first()
#     if employee:
#         db.delete(employee)
#         db.commit()
#     return employee


from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate

def create_employee(db: Session, emp: EmployeeCreate):
    new_emp = Employee(**emp.model_dump())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_employees(db: Session):
    return db.query(Employee).all()

def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

def update_employee(db: Session, emp_id: int, emp: EmployeeCreate):
    existing = db.query(Employee).filter(Employee.id == emp_id).first()
    if existing:
        for key, value in emp.model_dump().items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
    return existing

def delete_employee(db: Session, emp_id: int):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if emp:
        db.delete(emp)
        db.commit()
    return emp
