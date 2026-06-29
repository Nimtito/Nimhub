"""
=========================================================
NIMHUB
database/projects.py
=========================================================
"""

from datetime import datetime

from database.connection import connect


# =====================================================
# CREATE TABLE
# =====================================================

def create_projects_table():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            description TEXT,

            status TEXT NOT NULL,

            created_at TEXT NOT NULL,

            updated_at TEXT NOT NULL

        )
    """)

    conn.commit()
    conn.close()


# =====================================================
# ADD PROJECT
# =====================================================

def add_project(name, description, status):

    conn = connect()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO projects(

            name,
            description,
            status,
            created_at,
            updated_at

        )

        VALUES (?, ?, ?, ?, ?)
    """, (

        name,
        description,
        status,
        now,
        now

    ))

    conn.commit()
    conn.close()


# =====================================================
# GET ALL PROJECTS
# =====================================================

def get_all_projects():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM projects

        ORDER BY id DESC
    """)

    projects = cursor.fetchall()

    conn.close()

    return projects


# =====================================================
# GET PROJECT
# =====================================================

def get_project(project_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM projects

        WHERE id = ?
    """, (project_id,))

    project = cursor.fetchone()

    conn.close()

    return project

# =====================================================
# UPDATE PROJECT
# =====================================================

def update_project(project_id, name, description, status):

    conn = connect()
    cursor = conn.cursor()

    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE projects

        SET
            name = ?,
            description = ?,
            status = ?,
            updated_at = ?

        WHERE id = ?
    """, (

        name,
        description,
        status,
        updated_at,
        project_id

    ))

    conn.commit()
    conn.close()


# =====================================================
# DELETE PROJECT
# =====================================================

def delete_project(project_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM projects
        WHERE id = ?
    """, (project_id,))

    conn.commit()
    conn.close()


# =====================================================
# SEARCH PROJECTS
# =====================================================

def search_projects(keyword):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM projects

        WHERE
            name LIKE ?
            OR description LIKE ?

        ORDER BY id DESC
    """, (

        f"%{keyword}%",
        f"%{keyword}%"

    ))

    projects = cursor.fetchall()

    conn.close()

    return projects


# =====================================================
# LATEST PROJECTS
# =====================================================

def latest_projects(limit=5):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM projects

        ORDER BY id DESC

        LIMIT ?
    """, (limit,))

    projects = cursor.fetchall()

    conn.close()

    return projects


# =====================================================
# TOTAL PROJECTS
# =====================================================

def count_projects():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM projects
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# COMPLETED PROJECTS
# =====================================================

def count_completed_projects():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)

        FROM projects

        WHERE status = 'Completed'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# IN PROGRESS PROJECTS
# =====================================================

def count_in_progress_projects():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)

        FROM projects

        WHERE status = 'In Progress'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# CLEAR PROJECTS
# =====================================================

def clear_projects():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM projects
    """)

    conn.commit()
    conn.close()


# =====================================================
# INITIALIZE DATABASE
# =====================================================

create_projects_table()


# =====================================================
# TEST MODULE
# =====================================================

if __name__ == "__main__":

    print("=" * 50)
    print("Projects Database Ready")
    print("=" * 50)

    print("Total Projects :", count_projects())
    print("Completed :", count_completed_projects())
    print("In Progress :", count_in_progress_projects())