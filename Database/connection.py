"""
=========================================================
NIMHUB
database/connection.py
=========================================================
"""

import sqlite3
from pathlib import Path

# =====================================================
# DATABASE LOCATION
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE_PATH = BASE_DIR / "nimhub.db"

# =====================================================
# CONNECTION
# =====================================================

def connect():
    """
    Returns a SQLite connection.
    """

    return sqlite3.connect(DATABASE_PATH)