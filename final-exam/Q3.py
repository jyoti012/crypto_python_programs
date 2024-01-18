from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

def aes_tmto_encrypt(plaintext, initial_chain_value_hex, chain_length):
    # Convert the initial chain value from hex to bytes
    initial_chain_value = binascii.unhexlify(initial_chain_value_hex)

    # Convert plaintext to bytes and pad it (AES block size is 16 bytes)
    plaintext_bytes = pad(plaintext.encode(), AES.block_size)

    # Initialize the current key with the initial chain value
    current_key = initial_chain_value

    # Encrypt the plaintext 120 times, updating the key with the first 32 bytes of the encryption result
    for _ in range(chain_length):
        cipher = AES.new(current_key, AES.MODE_ECB)
        encrypted = cipher.encrypt(plaintext_bytes)
        # Use only the first 32 bytes of the encrypted output as the next key
        current_key = encrypted[:16]

    # Return the final chain value in hex
    return binascii.hexlify(current_key).decode()

# Input data
plaintext = "TMTOISTHEWAYTOGO"
initial_chain_value_hex = "db2a095620ed38d9cb57e654ccb47540"
chain_length = 100

# Perform the TMTO encryption
final_chain_value_hex = aes_tmto_encrypt(plaintext, initial_chain_value_hex, chain_length)

# Output the final chain value
print("Final Chain Value (Hex):", final_chain_value_hex)
