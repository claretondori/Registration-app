from fastapi import FastAPI
from pydantic import BaseModel
from routers import student, teacher, course
from models import create_table

app = FastAPI()

create_table()


app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(course.router)
























