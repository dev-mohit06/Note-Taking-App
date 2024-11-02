
# Note-Taking Application

## Overview
This command-line application allows users to create, view, edit, and delete notes. Notes are stored in a text file for persistence. 

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Understanding the Code](#understanding-the-code)
- [Submission](#submission)

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have Python installed on your machine. Python 3.6 or later is recommended.
- You have Git installed on your machine.

### Setting Up Python

#### Windows
1. **Download Python**: Go to [python.org/downloads](https://www.python.org/downloads/) and download the installer for Windows.
2. **Run the Installer**: Make sure to check the box that says "Add Python to PATH" during installation.
3. **Verify Installation**:
   - Open Command Prompt (cmd).
   - Run the following command:
     ```bash
     python --version
     ```

#### macOS
1. **Download Python**: Visit [python.org/downloads](https://www.python.org/downloads/) and download the installer for macOS.
2. **Run the Installer**: Follow the instructions to install Python.
3. **Verify Installation**:
   - Open Terminal.
   - Run the following command:
     ```bash
     python3 --version
     ```

#### Linux
1. **Install Python**: Use the package manager for your distribution. For example, on Ubuntu:
   ```bash
   sudo apt update
   sudo apt install python3
   ```
2. **Verify Installation**:
   - Open Terminal.
   - Run the following command:
     ```bash
     python3 --version
     ```

### Setting Up Git

#### Windows
1. **Download Git**: Go to [git-scm.com/downloads](https://git-scm.com/downloads) and download the installer for Windows.
2. **Run the Installer**: Follow the installation instructions, and you can choose default options.
3. **Verify Installation**:
   - Open Command Prompt (cmd).
   - Run the following command:
     ```bash
     git --version
     ```

#### macOS
1. **Install Git**: You can install Git using Homebrew. If you don’t have Homebrew installed, you can find it at [brew.sh](https://brew.sh).
   ```bash
   brew install git
   ```
2. **Verify Installation**:
   - Open Terminal.
   - Run the following command:
     ```bash
     git --version
     ```

#### Linux
1. **Install Git**: Use the package manager for your distribution. For example, on Ubuntu:
   ```bash
   sudo apt update
   sudo apt install git
   ```
2. **Verify Installation**:
   - Open Terminal.
   - Run the following command:
     ```bash
     git --version
     ```

## Installation
1. **Clone the Repository**:
   Open your terminal or command prompt and run the following command to clone the repository:
   ```bash
   git clone https://github.com/yourusername/note_taking_app.git
   ```
   Replace `yourusername` with your GitHub username.

2. **Navigate to the Project Directory**:
   ```bash
   cd note_taking_app/src
   ```

## Usage
1. **Usage.md**: [Click](./Usage.md) to see how to run the application

2. **Run the Application**:
   To run the application, execute the following command:
   ```bash
   python main.py
   ```
   (Use `python3` instead of `python` on macOS and Linux if required.)

3. **Follow the Prompts**:
   The application will present a menu with options to add, view, edit, and delete notes. Follow the prompts to interact with the application.

## Understanding the Code
The application consists of several modules:
- **`main.py`**: This is the main entry point for the application. It contains the main loop that handles user input and invokes functions from the other modules.
- **`notes_manager.py`**: This module handles all operations related to notes, such as loading, saving, adding, editing, and deleting notes.
- **`user_interface.py`**: This module is responsible for displaying the menu and handling user interactions.

### Code Explanation
- Each function in the `notes_manager.py` file is designed to perform a specific task. Students should implement the logic inside these functions to manage notes effectively.
- The user interface is designed to be user-friendly, guiding users through their options.

## Submission
1. **Complete Your Code**: Ensure that all functions in `notes_manager.py` are implemented and that your application works as expected.
2. **Create an text file**: Ensure you have created `explanation.txt` inside your project repository, detailing all functions in `notes_manager.py` and explaining how they work.
3. **Create a Zip File**: Once you are done, create a zip file of your project folder.
4. **Submit the Zip File**: Upload the `note_taking_app.zip` file to the designated submission portal.

Happy coding!