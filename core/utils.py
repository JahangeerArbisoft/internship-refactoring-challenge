# utils.py 

import time


def validate_email(email: str) -> bool:
    '''Basic email validation.'''
    return '@' in email and '.' in email

def hash_password(password: str) -> str:
    '''A very basic placeholder for password hashing (insecure).'''
    return password + "salt123"

def log_message(message: str):
    '''Logs message with timestamp.'''
    print(f"[{time.time()}] {message}")