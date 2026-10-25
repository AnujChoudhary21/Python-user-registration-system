"""
User Registration System

A simple user registration module that demonstrates:
- Validation functions
- Exception handling
- Duplicate checking
- Basic in-memory storage
"""


# -------------------------------------------------------------------
# Stimulate Database
# -------------------------------------------------------------------

registered_users = []
failed_registrations = []

# -------------------------------------------------------------------
# Validation functions
# -------------------------------------------------------------------

def validate_name(name: str):
    ''' 
        Validate that the name contains at least 3 characters.
    
        Args:
            name (str): The user's name.
    
        Returns:
            bool: True if valid, otherwise False.
        '''
    check1 = len(name) >= 3
    return check1


def validate_email(email):
    '''
        Validate that the email contains both '@' and '.'.
    
        Args:
            email (str): The user's email address.
    
        Returns:
            bool: True if valid, otherwise False.
        '''
    check2 = "@" in email and "." in email
    return check2


def validate_password(password: str) -> bool:
    '''
        Validate the password strength.
    
        Rules:
            - At least 8 characters long
            - Contains at least one uppercase letter
            - Contains at least one digit
    
        Args:
            password (str): The user's password.
    
        Returns:
            bool: True if valid, otherwise False.
        '''
    if len(password) < 8:
        return False

    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_uppercase and has_digit

# -------------------------------------------------------------------
# orchestrator function(Main validation function)
# -------------------------------------------------------------------

def validate_user_name(name, email, password):
    '''Validate all user inputs.
    
        Args:
            name (str): The user's name.
            email (str): The user's email.
            password (str): The user's password.
    
        Returns:
            bool: True if all validations pass.
    
        Raises:
            ValueError: If any validation rule fails.
        '''
    if not validate_name(name):
        raise ValueError("Length of name must be greater than 3 charcters.")
    if not validate_email(email):
        raise ValueError("Email must contain '@' and '.'.")
    if not validate_password(password):
        raise ValueError(
            "Password must be of 8 character with atleast one capital letter and one digit.")
    else:
        return True
    
# -------------------------------------------------------------------
# Create Registration user function
# -------------------------------------------------------------------

def create_user_account(name: str, email: str, password: str):
    '''Create a new user account after validation.
    
        Args:
            name (str): The user's name.
            email (str): The user's email.
            password (str): The user's password.
    
        Returns:
            dict: User dictionary if registration succeeds.
            None: If registration fails.
    
        Raises:
            ValueError: Internally raised during validation or duplicate checks.
        '''
    try:
        validate_user_name(name, email, password)
     
        if any(user["email"] == email for user in registered_users):
            raise ValueError("An account with this email already exist")
        else:
            user_dictionary = {
               "name": name,
               "email": email,
               "password": password,
               "status": "Active"
        }
        registered_users.append(user_dictionary)
        return user_dictionary
    except ValueError as error:
        failed_registrations.append(
            {"email":email, "error": error}
        )
    return None

# -------------------------------------------------------------------
# Testing Section
# -------------------------------------------------------------------

def run_tests():
    """
    Execute sample registration scenarios.

    Returns:
        None
    """
    test_cases = [
        ("Anuj", "anuj883@gmail.com", "Password1"),
        ("AnotherUser", "anuj883@gmail.com", "Password1"),
        ("An", "anuj7486@gmail.com", "Password1"),
        ("Harsh", "harsh.email.com", "Password1"),
        ("John", "john@email.com", "weakpass"),
    ]

    for index, (name, email, password) in enumerate(test_cases, start=1):
        print(f"\nTest {index}")
        result = create_user_account(name, email, password)

        if result:
            print("Registration successful:", result)
        else:
            print("Registration failed.")

    print("\nFinal Registered Users:")
    print(registered_users)

    print("\nFailed Registrations:")
    print(failed_registrations)



run_tests()






    



    

