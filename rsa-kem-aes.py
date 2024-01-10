from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
from hashlib import sha3_256
import os

def hex_string_to_bytes(hex_string):
    """ Convert a hex string to bytes """
    return bytes.fromhex(hex_string)

# Key decapsulation
clue = "6CA3B336F0CE95C6E39BC36D296C953B1638A8045923BA06BA21B6AD973386BCFE4A58F5C56EC8306F88F4C0FEEAA16CC13C97308014E4918D939266F3F7749185216162593795E7838A0CC0180E8800568C85E7D5880B5C7EFF6C5A65894468E705E12EB4D8DE1007C7CC2F2532C6EF4F39255488BE596E89A5AB530E3721A9A80EE297D746DD2252B66957839D0B6CBD35958AB8D7A0ED903A53730EB74DD5A2398D4E4912D78B04EC13A92A42D750D685C550FBD78CFC77BA8615892393C1970F8DADD6FD503D659DC52D12FEC6309085D02294AAED6B86AE79F6BAFCD529BDA23DD635FE306121C393FBE7F539E57C843A229476939FAC41330DD4BB4692"
cipher_text = hex_string_to_bytes(clue)

# Load private key (replace with the actual path to your key file)
with open("combined_keys.pem", "rb") as key_file:
    private_key = load_pem_private_key(key_file.read(), password=None)

# Decrypt with RSA
to_hash = private_key.decrypt(
    cipher_text,
    padding.PKCS1v15()
)

# Hash the result
key_arr = sha3_256(to_hash).digest()

# AES Decryption
aes_cipher_text_64 = "6VN3R6Dl7NLNaphNYXk7/BDMBFkk8d5tc/Mjp+fKx0I="
aes_cipher_text = base64.b64decode(aes_cipher_text_64)

# Create AES cipher
aes_key = key_arr[:32]  # Assuming AES-256, adjust the size accordingly
aes_cipher = Cipher(algorithms.AES(aes_key), modes.ECB())
decryptor = aes_cipher.decryptor()

plain_text = decryptor.update(aes_cipher_text) + decryptor.finalize()

print("Decrypted text:", plain_text.decode("utf-8"))
