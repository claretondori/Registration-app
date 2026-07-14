from fastapi import APIRouter
from schemas.teacher import Teacher

from repositories.teacher import(
    add_teacher,
    get_teachers,
    get_teacher,
    update_teacher,
    delete_teacher,
)

router = APIRouter(prefix="/teachers", tags= ["teachers"])

@router.get("")
def list_teachers():
    return get_teachers()

@router.get("/{teacher_id}")
def read_teacher(teacher_id: int):
    teacher = get_teacher(teacher_id)
    return teacher

@router.post("")
def register_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.email, teacher.subject, teacher.department, teacher.years_experience)
    return {"message": "Teacher registered", "teacher": teacher}

@router.put("/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    update_teacher(teacher_id, teacher.name, teacher.email, teacher.subject, teacher.department, teacher.years_experience)
    return {"message": "Teacher updated", "teacher": teacher}

@router.delete("/{teacher_id}")
def remove_teacher(teacher_id: int):
    delete_teacher(teacher_id)
    return {"message": "Teacher deleted"}





