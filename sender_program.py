# sender_program.py
"""
Sender Program (Client)
Sends the signed message to the receiver.
Author : Akash J
Roll No: 25MZ31
"""
import socket, json
from sender import Sender
from utils import print_separator, current_datetime

# --- VALID RSA KEY PAIR (FOR SIGNATURE) ---
# (p=43, q=59) -> n = 2537
# phi(n) = 2436
# e = 13, d = 937
# (13 * 937) % 2436 = 1
PRIVATE_KEY = 937
SIGNATURE_MODULUS = 2537  # This is 'n' (p*q)

HOST = '127.0.0.1'
PORT = 65432

# Create sender object
sender = Sender(PRIVATE_KEY, SIGNATURE_MODULUS)

# Step 1: Get sender message
sender_message = input("Enter Sender Message: ")

# Step 2: Generate hash and signature
full_hash, reduced_hash, signature = sender.sign_message(sender_message)

# Step 3: Prepare packet
packet = {
    "message": sender_message,
    "signature": signature,
    "full_hash": full_hash,
    "reduced_hash": reduced_hash
}

# Step 4: Send to receiver
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(packet).encode('utf-8'))

    print_separator()
    print(f"Sender Message   : {sender_message}")
    print(f"Full Hash        : {full_hash}")
    print(f"Reduced Hash     : {reduced_hash}")
    print(f"Digital Signature: {signature}")
    print(f"\n📨 Message delivered successfully at {current_datetime()}")
    print_separator()

except ConnectionRefusedError:
    print("\n[ERROR] Could not connect to receiver.")
    print("Please make sure receiver_program.py is running first.")