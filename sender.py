# sender.py
"""
Module: Sender
Handles message hashing and digital signature generation.
Author : Akash J
Roll No: 25MZ31
"""
from hashing import generate_hash

class Sender:
    def __init__(self, private_key: int, signature_modulus: int):
        self.private_key = private_key
        self.signature_modulus = signature_modulus  # This is the RSA modulus (n)

    def sign_message(self, message: str):
        """
        Generates a full hash, then reduces it using the
        signature modulus before signing.
        """
        # 1. Get the full, large hash
        full_hash = generate_hash(message)
        
        # 2. Reduce the hash to fit the signature key size
        #    This is the CRITICAL step.
        reduced_hash = full_hash % self.signature_modulus
        
        # 3. Sign the *reduced* hash
        signature = pow(reduced_hash, self.private_key, self.signature_modulus)
        
        return full_hash, reduced_hash, signature
