from storage import load_projects


def clear_screen():
    print("\n" * 3)


def stats_menu():
    clear_screen()
    print("=" * 45)
    print(" " * 13 + "DEVELOPER STATS")
    print("=" * 45)

    projects = load_projects()

    total_projects = len(projects)
    completed_projects = sum(1 for project in projects if project["status"] == "Completed")
    in_progress_projects = sum(1 for project in projects if project["status"] == "In Progress")

    print(f"Total Projects: {total_projects}")
    print(f"Completed: {completed_projects}")
    print(f"In Progress: {in_progress_projects}")

    input("\nPress ENTER to continue...")