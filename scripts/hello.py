#!/usr/bin/env python3
"""
A simple example script to get started with Python.
"""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Python scripting."


def main():
    """Main function to run the script."""
    user_name = input("What's your name? ")
    message = greet(user_name)
    print(message)
    print("\nYou've successfully run your first Python script!")


if __name__ == "__main__":
    main()
