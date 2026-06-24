from projects import projects_menu
from tools import tools_menu
from stats import stats_menu
from storage import initialize_data_file


def clear_screen():
    print("\n" * 3)


def show_welcome():
    clear_screen()
    print("=" * 45)
    print(" " * 16 + "NIMHUB")
    print(" " * 7 + "Developer Control Center")
    print("=" * 45)
    print("Welcome back, Developer 🚀")
    input("\nPress ENTER to continue...")


def main_menu():
    while True:
        clear_screen()
        print("=" * 45)
        print(" " * 13 + "MAIN DASHBOARD")
        print("=" * 45)
        print("1. Projects Manager")
        print("2. Tools")
        print("3. Developer Stats")
        print("4. Exit")
        print("=" * 45)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            projects_menu()
        elif choice == "2":
            tools_menu()
        elif choice == "3":
            stats_menu()
        elif choice == "4":
            clear_screen()
            print("Saving data...")
            print("Exiting NimHub...")
            print("Goodbye Developer!")
            break
        else:
            print("\nInvalid option. Please choose 1-4.")
            input("Press ENTER to continue...")


if __name__ == "__main__":
    initialize_data_file()
    show_welcome()
    main_menu()