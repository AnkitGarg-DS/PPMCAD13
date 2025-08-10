# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength 
# of the password. 
# ●       Implement a Python function called check_password_strength that takes a password string as input.
# ●       The function should check the password against the following criteria:
# ○       Minimum length: The password should be at least 8 characters long.
# ○       Contains both uppercase and lowercase letters.
# ○       Contains at least one digit (0-9).
# ○       Contains at least one special character (e.g., !, @, #, $, %).
# ●       The function should return a boolean value indicating whether the password meets the criteria.
# ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
# ●       Provide appropriate feedback to the user based on the strength of the password.

import re

def check_password_strength(password: str) -> bool:
    # Criteria Checks
    length_check = len(password) >= 8
    uppercase_check = re.search(r'[A-Z]', password) is not None
    lowercase_check = re.search(r'[a-z]', password) is not None
    digit_check = re.search(r'[0-9]', password) is not None
    special_char_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Return True if all criteria are met
    return all([length_check, uppercase_check, lowercase_check, digit_check, special_char_check])
    

# Main script to take user input and validate password strength
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    
    if check_password_strength(user_password):
        print("Your password is strong.")
    else:
        print("Your password is weak. Please ensure it meets the following criteria:")
        if len(user_password) < 8:
            print("- At least 8 characters long")
        if not re.search(r'[A-Z]', user_password):
            print("- Contains at least one uppercase letter")
        if not re.search(r'[a-z]', user_password):
            print("- Contains at least one lowercase letter")
        if not re.search(r'[0-9]', user_password):
            print("- Contains at least one digit (0-9)")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', user_password):
            print("- Contains at least one special character (e.g., !, @, #, $, %)")