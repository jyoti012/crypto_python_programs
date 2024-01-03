from Crypto.PublicKey import RSA
from hashlib import sha512

keyPair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

# compute S = h(m) d mod n where S is RSA signature, h(m) is Hash of message
# sign a message, using the RSA private key {n, d}.
# Calculate its hash and raise the hash to the power d modulo n (encrypt the hash by the private key).
# We shall use SHA-512 hash. It will fit in the current RSA key size (1024)

# RSA sign the message
msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
print("Hash: ", hash)
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

#  verify the signature, by decrypting the signature using the public key (raise the signature to power e modulo n) and
#  comparing the obtained hash from the signature to the hash of the originally signed message

# RSA verify signature
msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)

# RSA verify signature (tampered msg)
msg = b'A message for signing (tampered)'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid (tampered):", hash == hashFromSignature)

# Manually creating the RSA key pair with given n, e, and d
# keyPair = RSA.construct((n, e, d))

