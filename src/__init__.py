# __init__.py

"""
This package contains the modules for the Note-Taking Application.
"""

from .notes_manager import load_notes, save_notes, add_note, edit_note, delete_note
from .user_interface import display_menu, get_user_choice