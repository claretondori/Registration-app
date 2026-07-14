from pydantic import BaseModel

class Teacher(BaseModel):
    name:str
    email: str
    subject: str
    department: str
    years_experience: int 