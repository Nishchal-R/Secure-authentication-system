# main.py
# Entry-point skeleton: basic menu loop.

# Import authentication functions from auth module
from auth import register_user, login_user

# Display the main menu options to the user
def display_menu():
    print("\n=== Secure Auth System ===")
    print("1. Register  2. Login  3. Exit")

# Main program loop handling user input and routing to auth functions
def main():
    while True:
        display_menu()
        choice = input("Choice: ").strip()
        if choice == "1":

            # Register a new user with provided username and password
            register_user(input("Username: "), input("Password: "))
        elif choice == "2":
            # Login an existing user with provided credentials
            login_user(input("Username: "), input("Password: "))
        elif choice == "3":
            # Exit the program
            break
        else:
            print("Invalid option.")

# Run main() only when script is executed directly, not when imported
if __name__ == "__main__":
    main()