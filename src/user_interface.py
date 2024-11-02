# user_interface.py

def display_menu():
    # Display the menu options
    print("\nOptions:")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Exit")

def get_user_choice():
    # Get and return the user's menu choice
    choice = input("Choose an operation: ")
    return choice