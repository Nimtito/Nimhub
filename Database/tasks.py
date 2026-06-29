"""
=========================================================
NIMHUB
database/tasks.py
=========================================================
"""

from datetime import datetime

from database.connection import connect


# =====================================================
# CREATE TASKS TABLE
# =====================================================

def create_tasks_table():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            description TEXT,

            priority TEXT NOT NULL,

            status TEXT NOT NULL,

            due_date TEXT,

            created_at TEXT NOT NULL,

            updated_at TEXT NOT NULL

        )
    """)

    conn.commit()
    conn.close()


# =====================================================
# ADD TASK
# =====================================================

def add_task(
    title,
    description,
    priority,
    status,
    due_date
):

    conn = connect()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO tasks(

            title,
            description,
            priority,
            status,
            due_date,
            created_at,
            updated_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (

        title,
        description,
        priority,
        status,
        due_date,
        now,
        now

    ))

    conn.commit()
    conn.close()


# =====================================================
# GET ALL TASKS
# =====================================================

def get_all_tasks():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM tasks

        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    conn.close()

    return tasks


# =====================================================
# GET TASK
# =====================================================

def get_task(task_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM tasks

        WHERE id = ?
    """, (task_id,))

    task = cursor.fetchone()

    conn.close()

    return task

# =====================================================
# UPDATE TASK
# =====================================================

def update_task(
    task_id,
    title,
    description,
    priority,
    status,
    due_date
):

    conn = connect()
    cursor = conn.cursor()

    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE tasks

        SET
            title = ?,
            description = ?,
            priority = ?,
            status = ?,
            due_date = ?,
            updated_at = ?

        WHERE id = ?
    """, (

        title,
        description,
        priority,
        status,
        due_date,
        updated_at,
        task_id

    ))

    conn.commit()
    conn.close()
def complete_task(task_id):

    conn = connect()
    cursor = conn.cursor()

    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE tasks

        SET
            status = ?,
            updated_at = ?

        WHERE id = ?
    """, (

        "Completed",
        updated_at,
        task_id

    ))

    conn.commit()
    conn.close()

# =====================================================
# DELETE TASK
# =====================================================

def delete_task(task_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()


# =====================================================
# SEARCH TASKS
# =====================================================

def search_tasks(keyword):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM tasks

        WHERE
            title LIKE ?
            OR description LIKE ?

        ORDER BY id DESC
    """, (

        f"%{keyword}%",
        f"%{keyword}%"

    ))

    tasks = cursor.fetchall()

    conn.close()

    return tasks


# =====================================================
# LATEST TASKS
# =====================================================

def latest_tasks(limit=5):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM tasks

        ORDER BY id DESC

        LIMIT ?
    """, (limit,))

    tasks = cursor.fetchall()

    conn.close()

    return tasks


# =====================================================
# TOTAL TASKS
# =====================================================

def count_tasks():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# COMPLETED TASKS
# =====================================================

def count_completed_tasks():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)

        FROM tasks

        WHERE status = 'Completed'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# PENDING TASKS
# =====================================================

def count_pending_tasks():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)

        FROM tasks

        WHERE status = 'Pending'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# HIGH PRIORITY TASKS
# =====================================================

def count_high_priority_tasks():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)

        FROM tasks

        WHERE priority = 'High'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total

# =====================================================
# TOTAL TASKS
# =====================================================

def get_total_tasks():
    return count_tasks()


# =====================================================
# COMPLETED TASKS
# =====================================================

def get_completed_tasks():
    return count_completed_tasks()


# =====================================================
# PENDING TASKS
# =====================================================

def get_pending_tasks():
    return count_pending_tasks()


# =====================================================
# HIGH PRIORITY TASKS
# =====================================================

def get_high_priority_tasks():
    return count_high_priority_tasks()


# =====================================================
# TASK COMPLETION PERCENTAGE
# =====================================================

def task_completion_percentage():

    total = count_tasks()

    if total == 0:
        return 0

    completed = count_completed_tasks()

    return round((completed / total) * 100, 2)
# =====================================================
# CLEAR TASKS
# =====================================================

def clear_tasks():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
    """)

    conn.commit()
    conn.close()


# =====================================================
# INITIALIZE TABLE
# =====================================================

create_tasks_table()


# =====================================================
# TEST MODULE
# =====================================================

if __name__ == "__main__":

    print("=" * 50)
    print("Tasks Database Ready")
    print("=" * 50)

    print("Total Tasks :", count_tasks())
    print("Completed :", count_completed_tasks())
    print("Pending :", count_pending_tasks())
    print("High Priority :", count_high_priority_tasks())