import hashlib

def string_to_numerical_values(input_string):
    numerical_values = [ord(char) - ord('A') for char in input_string.upper()]
    return numerical_values

def convert_to_single_integer(numerical_values, base=26):
    result = 0
    for value in numerical_values:
        result = result * base + value
    return result

def generate_sha256_hash(plaintext_integer):
    plaintext_bytes = str(plaintext_integer).encode('utf-8')

    print("Original Message (String):", plaintext_string)
    print("Numerical Values of Each Character:", [ord(char) - ord('A') for char in plaintext_string.upper()])
    print("Single Integer Value:", plaintext_integer)
    print("Binary Representation of Single Integer:", bin(plaintext_integer)[2:])

    # Step 1: Padding
    padded_message = pad_message(plaintext_bytes)
    print("\nStep 1: Padding")
    print("Padded Message (in bits):", ''.join(f'{byte:08b}' for byte in padded_message))

    # Step 2: Initialize Hash Values (Simulated)
    hash_values = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    print("\nStep 2: Initialize Hash Values")
    print("Initial Hash Values (H0-H7):", [hex(value) for value in hash_values])

    # Step 3: Message Schedule (Simulated)
    message_schedule = []
    print("\nStep 3: Message Schedule (W0-W63):", message_schedule)

    # Step 4: Main Loop (Simulated)
    print("\nStep 4: Main Loop (64 iterations)")

    # Steps 5: SHA-256 Hash Calculation
    sha256_hash = hashlib.sha256(padded_message).hexdigest()

    print("\nFinal SHA-256 Hash:")
    print("Hash (in hexadecimal):", sha256_hash)

    return sha256_hash

def pad_message(message):
    message_length = len(message) * 8  # Length in bits

    # Append a single '1' bit
    padded_message = message + b'\x80'

    # Append '0' bits to reach a multiple of 512 bits less 64 bits
    padding_length = (448 - (message_length + 1) % 512) % 512
    padded_message += b'\x00' * (padding_length // 8)

    # Append the original message length as a 64-bit big-endian integer
    padded_message += message_length.to_bytes(8, 'big')

    return padded_message

# Public key and modulus
public_key_sender = 257
modulus_sender = 13837

# Plaintext
plaintext_string = "LLKJMLSTNRMGLIZKBW"
plaintext_numerical_values = string_to_numerical_values(plaintext_string)
plaintext_integer = convert_to_single_integer(plaintext_numerical_values)

# Generate SHA-256 hash for the plaintext
generate_sha256_hash(plaintext_integer)
