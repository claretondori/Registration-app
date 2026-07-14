from database import get_connection

def add_teacher(name , email,subject ,department, years_experience):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name, email,subject, department,years_experience) VALUES (?,?,?,?,?)',
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
    
def update_teacher(teacher_id, name, email, subject, department, years_experience):
    with get_connection() as connection:
        return connection.execute(
            'UPDATE teachers SET name = ?, email = ?, subject = ?, department = ?, years_experience = ? WHERE id = ?',
            (name, email, subject, department, years_experience, teacher_id)
        )

    
def delete_teacher(teacher_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id = ?', (teacher_id,))