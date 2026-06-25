def clear_screen():
    print("\n" * 3)


def open_nimtask():
    clear_screen()
    print("=" * 45)
    print(" " * 17 + "NIMTASK")
    print("=" * 45)
    print("Opening NimTask...")
    print("NimTask launcher placeholder for NimHub v1.0.")
    input("\nPress ENTER to continue...")


def open_nimfolio():
    clear_screen()
    print("=" * 45)
    print(" " * 16 + "NIMFOLIO")
    print("=" * 45)
    print("Opening Nimfolio...")
    print("Nimfolio launcher placeholder for NimHub v1.0.")
    input("\nPress ENTER to continue...")


def tools_menu():
    while True:
        clear_screen()
        print("=" * 45)
        print(" " * 18 + "TOOLS")
        print("=" * 45)
        print("1. NimTask")
        print("2. Nimfolio")
        print("3. Back")
        print("=" * 45)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            open_nimtask()
        elif choice == "2":
            open_nimfolio()
        elif choice == "3":
            break
        else:
            print("\nInvalid option. Please choose 1-3.")
            input("Press ENTER to continue...")