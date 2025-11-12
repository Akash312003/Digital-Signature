# receiver.py
"""
Module: Receiver
Verifies the authenticity of received messages.
Author : Akash J
Roll No: 25MZ31
"""
from hashing import generate_hash

class Receiver:
    def __init__(self, public_key: int, signature_modulus: int):
        self.public_key = public_key
        self.signature_modulus = signature_modulus # This is the RSA modulus (n)

    def verify_message(self, message: str, signature: int):
        """
        Verifies authenticity by re-hashing, reducing, 
        and comparing to the recovered hash.
        """
        # 1. Recompute the full, large hash from the received message
        recomputed_full_hash = generate_hash(message)
        
        # 2. Reduce it using the *same signature modulus*
        recomputed_reduced_hash = recomputed_full_hash % self.signature_modulus
        
        # 3. Recover the original reduced hash from the signature
        recovered_hash = pow(signature, self.public_key, self.signature_modulus)
        
        # 4. Compare the two reduced hashes
        is_authentic = (recomputed_reduced_hash == recovered_hash)
        
        return is_authentic, recomputed_full_hash, recomputed_reduced_hash, recovered_hash
