from cryptography.hazmat.primitives.asymmetric import ec
import hashlib

# P-256 curve parameters
curve = ec.SECP256R1()

# Alice's and Bob's private keys
priv_key_alice = 10007
priv_key_bob = 97123

# Generate keys for Alice and Bob
private_key_alice = ec.derive_private_key(priv_key_alice, curve)
private_key_bob = ec.derive_private_key(priv_key_bob, curve)

# Compute shared points
shared_point_alice = private_key_alice.exchange(ec.ECDH(), private_key_bob.public_key())
shared_point_bob = private_key_bob.exchange(ec.ECDH(), private_key_alice.public_key())

# Verification if shared points are identical
if shared_point_alice == shared_point_bob:
    print("Verification Successful: Shared points are identical.")
else:
    print("Verification Failed: Shared points are different.")


# Calculate the session key using SHA3-256 hash
sha3_hash = hashlib.sha3_256(shared_point_alice + shared_point_bob).digest()

# Convert the SHA3-256 hash to hexadecimal format
session_key_hex = sha3_hash.hex()

print('session_key_hex:', session_key_hex, '\n', 'shared_point_alice: ', shared_point_alice.hex(),
      '\n', 'shared_point_bob: ', shared_point_bob.hex());
