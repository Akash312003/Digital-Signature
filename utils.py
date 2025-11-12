# utils.py
"""
Module: Utility
Contains helper functions for formatting and time display.
Author : Akash J
Roll No: 25MZ31
"""
from datetime import datetime

def print_separator():
    """Prints a standard separator line."""
    print("----------------------------------------")

def current_datetime() -> str:
    """Returns the current date and time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_result(is_authentic: bool):
    """Displays the final authenticity result with an emoji."""
    if is_authentic:
        print("\n✅ The message is Authentic and Untampered.")
    else:
        print("\n❌ The message is Tampered or Invalid.")