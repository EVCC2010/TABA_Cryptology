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
hash_value = "403cdc63353976ed3aae0c8aa3da38f0a258b99b3da09a13cc10def74138633b"

# Sign the hash value using the sender's private key
signature = sign_hash(hash_value, d_sender, N_sender)

print("\nOriginal Hash:", hash_value)
print("Digital Signature:", signature)
