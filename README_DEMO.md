# Problematic Demo Project

This project is intentionally created with various bad practices for educational purposes.

## What's Wrong Here?

### Git Issues:
- No .gitignore file
- Sensitive data committed (config.py)
- Log files and cache files in version control
- Large dependencies without version pinning
- Binary/compiled files in repo (__pycache__)

### Python/PEP Issues:
- Mixed indentation (tabs vs spaces)
- Hardcoded sensitive information
- No type hints
- Poor function and variable naming
- Missing docstrings
- Unused imports
- Functions doing too many things
- No error handling
- Insecure password hashing
- Magic numbers and hardcoded values
- Long lines exceeding PEP 8 recommendations
- Inconsistent spacing around operators

### General Code Quality Issues:
- Global variables
- Tight coupling
- No separation of concerns
- Poor project structure
- Missing requirements versions
- No testing
- No proper logging configuration

## Your Task:
1. Identify all the issues
2. Create proper .gitignore
3. Refactor the code following PEP 8
4. Add proper error handling
5. Remove sensitive data
6. Improve project structure
7. Add documentation

Good luck! 