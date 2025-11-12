# hashing.py
"""
Module: Hashing Function
Generates a large, collision-resistant hash value.
Author : Akash J
Roll No: 25MZ31
"""

def generate_hash(message: str) -> int:
    """
    Generates a strong hash value for a message using polynomial rolling hash.
    A large base and very large prime modulus are chosen to prevent 
    collisions (e.g., "hello,guys" vs "hello guys").
    """
    base = 263                # A prime base > 256
    mod = 10000000019         # A very large prime (10 billion + 19)
    
    hash_value = 0
    for ch in message:
        hash_value = (hash_value * base + ord(ch)) % mod
        
    return hash_value

