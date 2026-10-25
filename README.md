# Python-user-registration-system
A Python registration workflow demonstrating input validation, exception handling, duplicate checking, and in-memory storage.

**Overview**
A beginner-friendly Python project that simulates a user registration system using input validation, exception handling, duplicate email detection, and in-memory storage.

**Features**

1. Name Validation: Checks that the user's name contains at least 3 characters.

2. Email Validation: Checks for the presence of @ and . in the email address.

3. Password Validation: Requires at least 8 characters, one uppercase letter, and one digit.

4. Duplicate Email Detection: Prevents registration when an email is already registered.

5. Exception Handling: Uses ValueError to handle invalid inputs and duplicate registrations.

6. Registration Tracking: Stores successful registrations and failed registration details in separate lists.

7. Orchestrator Function: Coordinates the validation and account-creation workflow.

8. Test Scenarios: Demonstrates successful registration and different validation failures.

**Technologies Used**

- Python 3

- Lists and dictionaries

- Functions and conditional statements

- Exception handling

- String manipulation and iteration

**Project Structure**

python-user-registration-system/
├── user_registration.py
└── README.md

**How to Run**
Install Python 3.

Clone or download this repository.

Open a terminal in the project directory.

Run:

user_registration.py

The script executes sample registration scenarios and displays the registration results.

**Concepts Practiced**

This project helped me practice modular programming, input validation, exception handling, duplicate checking, in-memory data management, and workflow orchestration in Python.

**Limitations**

User records are stored in memory and are lost when the program exits.

Email validation checks basic formatting only; it does not verify that an email address exists.

This is a learning project, not a production-ready authentication system.

**Future Improvements**

Add persistent storage using SQLite.

Implement secure password hashing.

Improve email validation and error reporting.

Add automated unit tests.

Separate the registration logic from the test runner.
