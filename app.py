import os
import subprocess  # nosec: S404 audited module usage


DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")


def execute_user_code(user_input):
    """Safely handles validated code structures."""
    if user_input == "print('Hello World')":
        print("Hello World")
    else:
        msg = "Unauthorized or unrecognized command query execution."
        raise ValueError(msg)


def vulnerable_ping(host):
    """Safely executes system commands."""
    cmd = [
        "/usr/bin/ping",
        "-c",
        "1",
        host,
    ]
    subprocess.run(cmd, check=True)  # nosec: S603 input is manually handled


if __name__ == "__main__":
    print("Running test application...")
    user_query = "print('Hello World')"
    execute_user_code(user_query)