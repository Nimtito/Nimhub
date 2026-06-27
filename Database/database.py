"""
database.py
---------------------------------------
Handles all SQLite database operations
for NimHub.
"""

import sqlite3
from pathlib import Path
from datetime import datetime

# ==========================================
# DATABASE LOCATION
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "nimhub.db"


# ==========================================
# CONNECTION
# ==========================================

def connect():
    """Create and return a database connection."""
    return sqlite3.connect(DATABASE)


# ==========================================
# CREATE DATABASE
# ==========================================

def create_database():
    """Create the projects table if it doesn't exist."""

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        description TEXT,

        status TEXT NOT NULL,

        date_created TEXT,

        last_updated TEXT

    )
    """)

    conn.commit()
    conn.close()


# ==========================================
# ADD PROJECT
# ==========================================

def add_project(name, description, status="In Progress"):

    conn = connect()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO projects
    (
        name,
        description,
        status,
        date_created,
        last_updated
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


# ==========================================
# GET ALL PROJECTS
# ==========================================

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


# ==========================================
# GET PROJECT BY ID
# ==========================================

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


# ==========================================
# UPDATE PROJECT
# ==========================================

def update_project(
        project_id,
        name,
        description,
        status
):

    conn = connect()

    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""

    UPDATE projects

    SET

    name=?,

    description=?,

    status=?,

    last_updated=?

    WHERE id=?

    """,

    (

        name,

        description,

        status,

        now,

        project_id

    ))

    conn.commit()

    conn.close()


# ==========================================
# DELETE PROJECT
# ==========================================

def delete_project(project_id):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

    DELETE FROM projects

    WHERE id=?

    """, (project_id,))

    conn.commit()

    conn.close()


# ==========================================
# SEARCH PROJECT
# ==========================================

def search_projects(keyword):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM projects

    WHERE name LIKE ?

       OR description LIKE ?

    """,

    (

        f"%{keyword}%",

        f"%{keyword}%"

    ))

    results = cursor.fetchall()

    conn.close()

    return results


# ==========================================
# COUNTS
# ==========================================

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


def count_completed_projects():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM projects

    WHERE status='Completed'

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def count_in_progress_projects():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM projects

    WHERE status='In Progress'

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==========================================
# CLEAR DATABASE
# ==========================================

def clear_database():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

    DELETE FROM projects

    """)

    conn.commit()

    conn.close()


# ==========================================
# INITIALIZE DATABASE
# ==========================================

create_database()


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    create_database()

    print("====================================")

    print("NimHub Database Ready")

    print("Database File :", DATABASE)

    print("Projects :", count_projects())

    print("====================================")