from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64decode

# Load the secret key (assuming it's in raw binary format)
with open("ChaCha20SecretKey.bin", "rb") as key_file:
    sk = key_file.read()

# Initialize the nonce
# nonce = bytearray([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x00, 0x00])
nonce = bytearray(16)
# Legible text and ciphertext
legible_text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()[]{};':\"/.,><?\n\t"
cipher_text64 = "+zUX+bJUJNFIERcZpZQr3+JkZRk="
cipher_text = b64decode(cipher_text64)

# Try to decrypt with different nonce values
for missing in range(0xffff):
    nonce[-2] = (missing >> 8) & 0xff
    nonce[-1] = missing & 0xff

    # Initialize cipher in decryption mode
    algorithm = algorithms.ChaCha20(sk, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    decryptor = cipher.decryptor()

    try:
        # Attempt to decrypt
        plain_text = decryptor.update(cipher_text) + decryptor.finalize()
        message = plain_text.decode('utf-8')

        # Check for legible text
        if all(char in legible_text for char in message):
            print("Decrypted message:", message)
            break
    except Exception:
        # Ignore exceptions and continue with the next nonce value
        pass
