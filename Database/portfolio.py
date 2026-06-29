"""
=========================================================
NIMHUB
database/portfolio.py
=========================================================
"""

from database.connection import connect


# =====================================================
# CREATE PORTFOLIO TABLE
# =====================================================

def create_portfolio_table():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS portfolio(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            profession TEXT,

            location TEXT,

            about TEXT,

            phone TEXT,

            email TEXT,

            github TEXT,

            linkedin TEXT,

            website TEXT

        )
    """)

    conn.commit()
    conn.close()


# =====================================================
# SAVE PORTFOLIO
# =====================================================

def save_portfolio(
    full_name,
    profession,
    location,
    about,
    phone,
    email,
    github,
    linkedin,
    website
):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM portfolio")

    cursor.execute("""
        INSERT INTO portfolio(

            full_name,
            profession,
            location,
            about,
            phone,
            email,
            github,
            linkedin,
            website

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        full_name,
        profession,
        location,
        about,
        phone,
        email,
        github,
        linkedin,
        website

    ))

    conn.commit()
    conn.close()


# =====================================================
# LOAD PORTFOLIO
# =====================================================

def load_portfolio():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *

        FROM portfolio

        LIMIT 1
    """)

    profile = cursor.fetchone()

    conn.close()

    return profile

# =====================================================
# UPDATE PORTFOLIO
# =====================================================

def update_portfolio(
    full_name,
    profession,
    location,
    about,
    phone,
    email,
    github,
    linkedin,
    website
):

    conn = connect()
    cursor = conn.cursor()

    profile = load_portfolio()

    if profile is None:

        conn.close()

        save_portfolio(
            full_name,
            profession,
            location,
            about,
            phone,
            email,
            github,
            linkedin,
            website
        )

        return

    cursor.execute("""
        UPDATE portfolio

        SET

            full_name = ?,
            profession = ?,
            location = ?,
            about = ?,
            phone = ?,
            email = ?,
            github = ?,
            linkedin = ?,
            website = ?

        WHERE id = ?

    """, (

        full_name,
        profession,
        location,
        about,
        phone,
        email,
        github,
        linkedin,
        website,
        profile[0]

    ))

    conn.commit()
    conn.close()


# =====================================================
# CLEAR PORTFOLIO
# =====================================================

def clear_portfolio():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM portfolio
    """)

    conn.commit()
    conn.close()


# =====================================================
# PORTFOLIO EXISTS
# =====================================================

def portfolio_exists():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)

        FROM portfolio
    """)

    exists = cursor.fetchone()[0] > 0

    conn.close()

    return exists


# =====================================================
# INITIALIZE TABLE
# =====================================================

create_portfolio_table()


# =====================================================
# TEST MODULE
# =====================================================

if __name__ == "__main__":

    print("=" * 50)
    print("Portfolio Database Ready")
    print("=" * 50)

    if portfolio_exists():
        print("Portfolio Found")
    else:
        print("No Portfolio Saved")