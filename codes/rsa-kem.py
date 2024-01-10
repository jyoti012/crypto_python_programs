import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encapsulate_key(public_key):
    session_key = os.urandom(32)  # Generate a 256-bit session key
    encapsulated_key = public_key.encrypt(
        session_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return session_key, encapsulated_key

def decapsulate_key(private_key, encapsulated_key):
    session_key = private_key.decrypt(
        encapsulated_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return session_key

# Generate RSA keys
private_key, public_key = generate_rsa_keys()

# Encapsulate a session key
original_session_key, encapsulated_key = encapsulate_key(public_key)

# Decapsulate the session key
decapsulated_session_key = decapsulate_key(private_key, encapsulated_key)

# Check if the original and decapsulated session keys are the same
assert original_session_key == decapsulated_session_key
print("Session key successfully encapsulated and decapsulated.")
print('original session key: ', original_session_key)
print('decapsulated key: ', decapsulated_session_key)
# Convert the decapsulated session key to decimal and hexadecimal formats
decapsulated_key_decimal = int.from_bytes(decapsulated_session_key, byteorder='big')
decapsulated_key_hex = decapsulated_session_key.hex()

print(decapsulated_key_decimal, decapsulated_key_hex)
