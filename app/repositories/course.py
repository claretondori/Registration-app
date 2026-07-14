from database import get_connection

def add_course(title, code , credits,department ,teacher_id):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses (title,code , credits,department, teacher_id) VALUES (?,?,?,?,?)',
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
        return connection.execute('UPDATE  courses SET title = ?, code =?, credits =?, department = ?, teacher_id = ? WHERE id = ?',(course_id, title,code , credits, department, teacher_id))
    
def delete_course(course_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE id = ?', (course_id,))