def password_strength_counter(password):
    strength = {
        'length': 'False',
        'digit': 'False',
        'lowercase': 'False',
        'uppercase': 'False'
    }
    if len(password) >= 8:
        strength['length'] = 'True'
    for char in password:
        if char.isdigit():
            strength['digit'] = 'True'
        if char.islower():
            strength['lowercase'] = 'True'
        if char.isupper():
            strength['uppercase'] = 'True'
    return strength

#Multiple passwords strength check
def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"

    all_password_strengths = []  # To store strength for each password

    for password in passwords:
        # Initialize strength for the current password
        strength = {
            'length': False,
            'digit': False,
            'lowercase': False,
            'uppercase': False,
            'special_char': False
        }

        # Check each condition for the current password
        if len(password) >= 8:
            strength['length'] = True

        if any(char.isdigit() for char in password):
            strength['digit'] = True

        if any(char.islower() for char in password):
            strength['lowercase'] = True

        if any(char.isupper() for char in password):
            strength['uppercase'] = True

        if any(char in special_characters for char in password):
            strength['special_char'] = True

        # Append the strength result of the current password to the list
        all_password_strengths.append(strength)

    return all_password_strengths
