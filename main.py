# main.py
"""
Main Controller
Simulates the Digital Signature Verification process using hashing.
Author : Akash J
Roll No: 25MZ31
"""

from sender import Sender
from receiver import Receiver
from utils import print_separator, print_result

def main():
    print_separator()
    print(" DIGITAL SIGNATURE VERIFICATION USING HASHING (SIMULATION) ")
    print_separator()

    # Educational constants (for demo)
    private_key = 37
    public_key = 13
    modulus = 2537

    # Create sender and receiver objects
    sender = Sender(private_key, modulus)
    receiver = Receiver(public_key, modulus)

    # Input messages
    sender_message = input("\nEnter the Sender Message: ")
    receiver_message = input("Enter the Receiver Message: ")

    # Sender signs the message
    sender_hash, signature = sender.sign_message(sender_message)

    # Receiver verifies authenticity
    is_authentic = receiver.verify_message(receiver_message, signature)

    # Display results
    print_separator()
    print(f"Sender Message   : {sender_message}")
    print(f"Receiver Message : {receiver_message}")
    print(f"Generated Hash   : {sender_hash}")
    print(f"Digital Signature: {signature}")
    print_result(is_authentic)
    print_separator()


if __name__ == "__main__":
    main()
