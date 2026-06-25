import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection 
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_connection() as connection:
        connection.execute(''' CREATE TABLE IF NOT EXISTS students(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL
                           )''')
        
        connection.execute(''' CREATE TABLE IF NOT EXISTS teachers (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           email TEXT NOT NULL,
                           subject TEXT NOT NULL,
                           department TEXT NOT NULL,
                           years_experience INTEGER NOT NULL
                           )'''

        )

        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL, 
                           code TEXT NOT NULL,
                           credits INTEGER NOT NULL,
                           department TEXT NOT NULL,
                           teacher_id INTEGER,
                           FOREIGN KEY(teacher_id) REFERENCES teachers (id)
                           )'''

        )



def add_student(name,age , email,country ,id_number):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students (name,age , email,country, id_number) VALUES (?,?,?,?,?)',
            (name,age , email,country ,id_number)
        )

def get_students():
    with get_connection() as  connection:
        return connection.execute('SELECT * FROM students').fetchall()

def get_student(student_id):
    with get_connection() as connection:
        return connection.execute(
            'SELECT * FROM students WHERE id = ?', (student_id,)
        ).fetchone()
    
def update_student(student_id, name,age , email, country, id_number):
    with get_connection() as connection:
        return connection.execute('UPDATE  students SET name = ?, age =?, email =?, country = ?, id_number = ? WHERE id = ?',(name, age, email, country, id_number,student_id))
    
def delete_student(student_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM students WHERE id = ?', (student_id))




















def add_course(title, code , credits,department ,teacher_id):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students (title,code , credits,department, teacher_id) VALUES (?,?,?,?,?)',
            (title,code , credits,department ,teacher_id)
        )

def get_courses():
    with get_connection() as  connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def get_course(course_id):
    with get_connection() as connection:
        return connection.execute(
            'SELECT * FROM courses WHERE id = ?', (course_id,)
        ).fetchone()
    
def update_course(course_id, title,code , credits, department, teacher_id):
    with get_connection() as connection:
        return connection.execute('UPDATE  students SET title = ?, code =?, credits =?, department = ?, teacher_id = ? WHERE id = ?',(course_id, title,code , credits, department, teacher_id))
    
def delete_course(course_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE id = ?', (course_id))






















def add_teacher(name , email,subject ,department, years_experience):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students (name, email,subject, department,years_experience) VALUES (?,?,?,?,?)',
            (name , email,subject ,department, years_experience)
        )

def get_teachers():
    with get_connection() as  connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def get_teacher(teacher_id):
    with get_connection() as connection:
        return connection.execute(
            'SELECT * FROM teachers WHERE id = ?', (teacher_id,)
        ).fetchone()
    
def update_teacher(teacher_id, name , email, subject, department, years_experience):
    with get_connection() as connection:
        return connection.execute('UPDATE  students SET teacher_id = ?, name =?, email =?, subject = ?, department = ? , years_experience = ?, WHERE id = ?',(teacher_id, name , email, subject, department, years_experience))
    
def delete_teacher(teacher_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id = ?', (teacher_id))