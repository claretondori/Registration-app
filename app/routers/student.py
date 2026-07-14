from fastapi import APIRouter
from schemas.student import Student

from repositories.student import(
    add_student,
    get_students,
    get_student,
    update_student,
    delete_student,
)

router = APIRouter(prefix="/students", tags= ["students"])

@router.get("")
def home():
    return {"message":"welcome to my API"}

@router.get("")
def list_students():
    students = get_students()
    return students

@router.get("/{student_id}")
def read_student(student_id: int):
    student = get_student(student_id)
    return student 

@router.post("")
def register_student(student:Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message":"Student registered","student":student}


@router.put("/{student_id}")
def edit_student(student_id: int,student:Student):
    update_student(student_id,student.name, student.age, student.email, student.country, student.id_number)
    return {"message":"Student updated","student":student}


@router.delete("/{student_id}")
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message":"Student deleted"}