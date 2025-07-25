# user_processing.py

from utils import validate_email, hash_password

def process_user_data(users: list[dict]) -> list[dict]:
    '''Filters and process user data - adults with valid emails.'''
    processed = []

    for user in users:
        if user.get('age', 0) >= 18 and validate_email(user.get('email', '')):
            new_user = user.copy()
            new_user['password'] = hash_password(new_user['password'])
            processed.append(new_user)
    
    return processed