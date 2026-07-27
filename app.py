import os
import sys  # Flake8 (F401): Unused import

# Bandit (B105): Hardcoded password string literal
DATABASE_PASSWORD = "super_secret_password_123"


def execute_user_code(user_input):
    """Executes arbitrary string commands from a user."""
    # Bandit (B102): Use of exec is a major security vulnerability
    exec(user_input)


def vulnerable_ping(host):
    # Flake8 (E225): Missing whitespace around operator
    # Bandit (B605/B607): Starting a process with a shell / partial executable path
    cmd = "ping -c 1 " + host
    os.system(cmd)


if __name__ == "__main__":
    print("Running test application...")
    # Flake8 (W291): Trailing whitespace at the end of the line below  
    user_query = "print('Hello World')"
    execute_user_code(user_query)
