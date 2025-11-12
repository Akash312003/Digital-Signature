# receiver_program.py
"""
Receiver Program (Server)
Receives message and verifies authenticity, then saves a report.
Author : Akash J
Roll No: 25MZ31
"""
import socket, json, os
from datetime import datetime
from receiver import Receiver
from utils import print_separator, print_result
from hashing import generate_hash # Import for the report

# --- VALID RSA KEY PAIR (FOR SIGNATURE) ---
PUBLIC_KEY = 13
SIGNATURE_MODULUS = 2537 # Must match sender's modulus

HOST = '127.0.0.1'
PORT = 65432

receiver = Receiver(PUBLIC_KEY, SIGNATURE_MODULUS)

def save_verification_report(sender_msg, receiver_msg, sender_full_hash, 
                             receiver_full_hash, sender_reduced_hash, 
                             receiver_reduced_hash, recovered_hash, sig, is_auth):
    """Creates a detailed verification report."""
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join("reports", f"verification_report_{timestamp}.txt")
    
    result_text = "✅ The message is Authentic" if is_auth else "❌ The message is Tampered or Invalid"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("----------------------------------------\n")
        f.write(" Digital Signature Verification Report\n")
        f.write("----------------------------------------\n")
        f.write(f"Verification Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Sender Message    : {sender_msg}\n")
        f.write(f"Receiver Message  : {receiver_msg}\n\n")
      
        
        f.write("--- SIGNATURE (Verification Check) ---\n")
        f.write(f"Sender Reduced Hash   : {sender_reduced_hash}\n")
        f.write(f"Receiver Reduced Hash : {receiver_reduced_hash}\n")
        f.write(f"Recovered Hash (from sig): {recovered_hash}\n")
        f.write(f"Digital Signature : {sig}\n\n")
        
        f.write("--- FINAL RESULT ---\n")
        f.write(f"{result_text}\n")
        f.write("----------------------------------------\n")

    print(f"\n📝 Report saved successfully as: {filename}\n")

print("Receiver is waiting for connection...\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    conn, addr = server_socket.accept()
    
    with conn:
        print(f"Connected to Sender: {addr}\n")
        data = conn.recv(4096).decode('utf-8')
        packet = json.loads(data)
        
        sender_message = packet["message"]
        signature = int(packet["signature"])
        sender_full_hash = int(packet["full_hash"])
        sender_reduced_hash = int(packet["reduced_hash"])

        receiver_message = input("Enter Receiver Message: ")

        is_auth, rec_full, rec_reduced, rec_recovered = receiver.verify_message(
            receiver_message, signature
        )

        print_separator()
        print(f"Sender Message   : {sender_message}")
        print(f"Receiver Message : {receiver_message}")
        print_result(is_auth)
        print_separator()
        
        save_verification_report(
            sender_message, receiver_message, sender_full_hash,
            rec_full, sender_reduced_hash, rec_reduced,
            rec_recovered, signature, is_auth
        )