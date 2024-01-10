# from tinyec import registry
# import secrets
#
# def compress(pubKey):
#  return hex(pubKey.x) + hex(pubKey.y % 2)[2:]
#
# curve = registry.get_curve('brainpoolP256r1')
# print(curve.g)
#
# alicePrivKey = secrets.randbelow(curve.field.n)
# alicePubKey = alicePrivKey * curve.g
# print("Alice public key:", compress(alicePubKey))
#
# bobPrivKey = secrets.randbelow(curve.field.n)
# bobPubKey = bobPrivKey * curve.g
# print("Bob public key:", compress(bobPubKey))
#
# print("Now exchange the public keys (e.g. through Internet)")
#
# aliceSharedKey = alicePrivKey * bobPubKey
# print("Alice shared key:", compress(aliceSharedKey))
#
# bobSharedKey = bobPrivKey * alicePubKey
# print("Bob shared key:", compress(bobSharedKey))
#
# print("Equal shared keys:", aliceSharedKey == bobSharedKey)

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate a private key for use in the elliptic curve key exchange algorithm
private_key = ec.generate_private_key(ec.SECP256R1())

# Serialize the private key to PEM format
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Display the private key
print("Private Key:")
print(pem_private_key.decode())

# Get the public key corresponding to the private key
public_key = private_key.public_key()

# Serialize the public key to PEM format
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Display the public key
print("Public Key:")
print(pem_public_key.decode())

