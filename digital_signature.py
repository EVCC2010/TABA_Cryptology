import hashlib

def sign_hash(hash_value, private_key, modulus):
    # Use RSA private key to sign the hash value
    hash_int = int(hash_value, 16)

    print("\nStep 1: Convert Hash Value to Integer")
    print("Hash Value (Integer):", hash_int)

    signature = pow(hash_int, private_key, modulus)

    print("\nStep 2: Calculate Digital Signature")
    print("Signature (M^d mod N):", signature)

    return signature

# Sender's private key and modulus
d_sender = 2593
N_sender = 13837

# Hash value obtained
hash_value = "e8bd46fb89f461824baa007e4afc5d269b52a3b5b7cb40e1d6fa6509ce05348a"

# Sign the hash value using the sender's private key
signature = sign_hash(hash_value, d_sender, N_sender)

print("\nOriginal Hash:", hash_value)
print("Digital Signature:", signature)
