"""
=========================================================
NIMHUB
database/statistics.py
=========================================================
"""

from database.projects import (
    count_projects,
    count_completed_projects,
    count_in_progress_projects
)

from database.tasks import (
    count_tasks,
    count_completed_tasks,
    count_pending_tasks,
    count_high_priority_tasks
)

from database.portfolio import (
    portfolio_exists
)


# =====================================================
# DASHBOARD SUMMARY
# =====================================================

def dashboard_summary():

    return {

        "projects": count_projects(),

        "completed_projects": count_completed_projects(),

        "in_progress_projects": count_in_progress_projects(),

        "tasks": count_tasks(),

        "completed_tasks": count_completed_tasks(),

        "pending_tasks": count_pending_tasks(),

        "high_priority_tasks": count_high_priority_tasks(),

        "portfolio": portfolio_exists()

    }


# =====================================================
# PROJECT STATISTICS
# =====================================================

def project_statistics():

    return {

        "total": count_projects(),

        "completed": count_completed_projects(),

        "in_progress": count_in_progress_projects()

    }


# =====================================================
# TASK STATISTICS
# =====================================================

def task_statistics():

    return {

        "total": count_tasks(),

        "completed": count_completed_tasks(),

        "pending": count_pending_tasks(),

        "high_priority": count_high_priority_tasks()

    }


# =====================================================
# PORTFOLIO STATUS
# =====================================================

def portfolio_statistics():

    return {

        "exists": portfolio_exists()

    }


# =====================================================
# COMPLETE SYSTEM REPORT
# =====================================================

def system_statistics():

    return {

        "projects": project_statistics(),

        "tasks": task_statistics(),

        "portfolio": portfolio_statistics()

    }


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    print("=" * 50)

    print("NimHub Statistics Module")

    print("=" * 50)

    print(system_statistics())