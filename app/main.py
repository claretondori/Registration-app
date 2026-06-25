from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table, add_student,get_students, get_student, update_student,delete_student, add_teacher, get_teachers, get_teacher,update_teacher,delete_teacher, add_course,get_courses,get_course,update_course,delete_course


app = FastAPI()

create_table()

class Student(BaseModel):
    name:str
    age: int
    email:str
    country: str
    id_number: int

class Teacher(BaseModel):
    name:str
    email: str
    subject: str
    department: str
    years_experience: int 

class Courses(BaseModel):
    title: str
    code: str
    credits: int 
    department: str
    teacher_id: int 



students = []


@app.get("/")
def home():
    return {"message":"welcome to my API"}

@app.get("/students")
def list_students():
    students = get_students()
    return students

@app.get("/students/{student_id}")
def read_student(student_id: int):
    student = get_student(student_id)
    return student 

@app.post("/students")
def register_student(student:Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message":"Student registered","student":student}


@app.put("/students/{student_id}")
def edit_student(student_id: int,student:Student):
    update_student(student_id,student.name, student.age, student.email, student.country, student.id_number)
    return {"message":"Student updated","student":student}


@app.delete("/students/{student_id}")
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message":"Student deleted"}








@app.get("/teachers")
def list_teachers():
    return get_teachers()

@app.get("/teachers/{teacher_id}")
def read_teacher(teacher_id: int):
    teacher = get_teacher(teacher_id)
    return teacher

@app.post("/teachers")
def register_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.email, teacher.subject, teacher.department, teacher.years_experience)
    return {"message": "Teacher registered", "teacher": teacher}

@app.put("/teachers/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    update_teacher(teacher_id, teacher.name, teacher.email, teacher.subject, teacher.department, teacher.years_experience)
    return {"message": "Teacher updated", "teacher": teacher}

@app.delete("/teachers/{teacher_id}")
def remove_teacher(teacher_id: int):
    delete_teacher(teacher_id)
    return {"message": "Teacher deleted"}







@app.get("/courses")
def list_courses():
    return get_courses()

@app.get("/courses/{course_id}")
def read_course(course_id: int):
    course = get_course(course_id)
    return course

@app.post("/courses")
def register_course(course: Courses):
    add_course(course.title, course.code, course.credits, course.department, course.teacher_id)
    return {"message": "Course registered", "course": course}

@app.put("/courses/{course_id}")
def edit_course(course_id: int, course: Courses):
    update_course(course_id, course.title, course.code, course.credits, course.department, course.teacher_id)
    return {"message": "Course updated", "course": course}

@app.delete("/courses/{course_id}")
def remove_course(course_id: int):
    delete_course(course_id)
    return {"message": "Course deleted"}




