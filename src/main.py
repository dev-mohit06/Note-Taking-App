# main.py

from user_interface import display_menu, get_user_choice
from notes_manager import load_notes, save_notes, add_note, edit_note, delete_note, view_notes

def main():
    notes = load_notes()  # Load existing notes
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            add_note(notes, title, content)  # Implement add_note in notes_manager
        elif choice == '2':
            view_notes(notes)  # Implement view_notes in notes_manager
        elif choice == '3':
            index = int(input("Enter note index to edit: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            edit_note(notes, index, new_title, new_content)  # Implement edit_note in notes_manager
        elif choice == '4':
            index = int(input("Enter note index to delete: "))
            delete_note(notes, index)  # Implement delete_note in notes_manager
        elif choice == '5':
            save_notes(notes)  # Save notes before exiting
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()