from storage import load_projects, save_projects


def clear_screen():
    print("\n" * 3)


def display_projects(projects):
    if not projects:
        print("\nNo projects found.")
        return

    print("\nSaved Projects:")
    print("-" * 70)
    for index, project in enumerate(projects, start=1):
        print(f"{index}. {project['name']}")
        print(f"   Description: {project['description']}")
        print(f"   Status: {project['status']}")
        print("-" * 70)


def add_project():
    clear_screen()
    print("=" * 45)
    print(" " * 14 + "ADD PROJECT")
    print("=" * 45)

    name = input("Project name: ").strip()
    if not name:
        print("\nProject name cannot be empty.")
        input("Press ENTER to continue...")
        return

    description = input("Project description: ").strip()
    if not description:
        description = "No description provided"

    while True:
        print("\nChoose project status:")
        print("1. In Progress")
        print("2. Completed")
        status_choice = input("Enter choice: ").strip()

        if status_choice == "1":
            status = "In Progress"
            break
        elif status_choice == "2":
            status = "Completed"
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

    projects = load_projects()

    # prevent duplicate project names
    for project in projects:
        if project["name"].lower() == name.lower():
            print("\nA project with that name already exists.")
            input("Press ENTER to continue...")
            return

    new_project = {
        "name": name,
        "description": description,
        "status": status
    }

    projects.append(new_project)
    save_projects(projects)

    print(f"\nProject '{name}' added successfully.")
    input("Press ENTER to continue...")


def view_projects():
    clear_screen()
    print("=" * 45)
    print(" " * 13 + "VIEW PROJECTS")
    print("=" * 45)

    projects = load_projects()
    display_projects(projects)

    input("\nPress ENTER to continue...")


def update_project_status():
    clear_screen()
    print("=" * 45)
    print(" " * 9 + "UPDATE PROJECT STATUS")
    print("=" * 45)

    projects = load_projects()

    if not projects:
        print("\nNo projects available to update.")
        input("Press ENTER to continue...")
        return

    display_projects(projects)

    try:
        project_number = int(input("\nEnter project number to update: ").strip())
        if project_number < 1 or project_number > len(projects):
            print("Invalid project number.")
            input("Press ENTER to continue...")
            return
    except ValueError:
        print("Please enter a valid number.")
        input("Press ENTER to continue...")
        return

    while True:
        print("\nSet new status:")
        print("1. In Progress")
        print("2. Completed")
        status_choice = input("Enter choice: ").strip()

        if status_choice == "1":
            new_status = "In Progress"
            break
        elif status_choice == "2":
            new_status = "Completed"
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

    selected_project = projects[project_number - 1]
    selected_project["status"] = new_status
    save_projects(projects)

    print(f"\nProject '{selected_project['name']}' updated successfully.")
    input("Press ENTER to continue...")


def delete_project():
    clear_screen()
    print("=" * 45)
    print(" " * 13 + "DELETE PROJECT")
    print("=" * 45)

    projects = load_projects()

    if not projects:
        print("\nNo projects available to delete.")
        input("Press ENTER to continue...")
        return

    display_projects(projects)

    try:
        project_number = int(input("\nEnter project number to delete: ").strip())
        if project_number < 1 or project_number > len(projects):
            print("Invalid project number.")
            input("Press ENTER to continue...")
            return
    except ValueError:
        print("Please enter a valid number.")
        input("Press ENTER to continue...")
        return

    removed_project = projects.pop(project_number - 1)
    save_projects(projects)

    print(f"\nProject '{removed_project['name']}' deleted successfully.")
    input("Press ENTER to continue...")


def projects_menu():
    while True:
        clear_screen()
        print("=" * 45)
        print(" " * 12 + "PROJECTS MANAGER")
        print("=" * 45)
        print("1. Add Project")
        print("2. View Projects")
        print("3. Update Project Status")
        print("4. Delete Project")
        print("5. Back")
        print("=" * 45)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_project()
        elif choice == "2":
            view_projects()
        elif choice == "3":
            update_project_status()
        elif choice == "4":
            delete_project()
        elif choice == "5":
            break
        else:
            print("\nInvalid option. Please choose 1-5.")
            input("Press ENTER to continue...")