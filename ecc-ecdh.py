# from sympy import mod_inverse
# # def mod_inverse(a, m):
# #     """Compute the modular inverse of a modulo m."""
# #     return pow(a, -1, m)
#
# def elliptic_curve_addition(P, Q, A, p):
#     """Perform addition on the elliptic curve."""
#     if P == Q:  # Doubling
#         slope = (3 * P[0]**2 + A) * mod_inverse(2 * P[1], p) % p
#     else:  # Point addition
#         slope = (Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p) % p
#
#     x3 = (slope**2 - P[0] - Q[0]) % p
#     y3 = (slope * (P[0] - x3) - P[1]) % p
#
#     return (x3, y3)
#
# def ecc_scalar_multiplication(k, G, A, B, p):
#     """Perform scalar multiplication k*G on an elliptic curve."""
#     result = G
#     for _ in range(k - 1):
#         result = elliptic_curve_addition(result, G, A, p)
#     return result
#
# # Example usage
# A = 115792089210356248762697446949407573530086143415290314195533631308867097853948
# B = 41058363725152142129326129780047268409114441015993725554835256314039467401291
# p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
# G = (48439561293906451759052585252797914202762949526041747995844080717082404635286,
#      36134250956749795798585127919587881956611106672985015071877270311162452333045)
#
# # Alice's and Bob's private keys
# priv_key_alice = 10007
# priv_key_bob = 97123
#
# # Calculate public keys
# alice_public_key = ecc_scalar_multiplication(priv_key_alice, G, A, B, p)
# bob_public_key = ecc_scalar_multiplication(priv_key_bob, G, A, B, p)
#
# print("Alice's Public Key:", alice_public_key)
# print("Bob's Public Key:", bob_public_key)
#
# #
# # # Curve parameters
# # A = 115792089210356248762697446949407573530086143415290314195533631308867097853948
# # B = 41058363725152142129326129780047268409114441015993725554835256314039467401291
# # p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
# #
# # # Generator point G
# # G = (48439561293906451759052585252797914202762949526041747995844080717082404635286,
# #      36134250956749795798585127919587881956611106672985015071877270311162452333045)
# #
# # # Alice's and Bob's private keys
# # priv_key_alice = 10007
# # priv_key_bob = 97123
# #
# # # Calculate public keys
# # alice_public_key = ecc_scalar_multiplication(priv_key_alice, G, A, B, p)
# # bob_public_key = ecc_scalar_multiplication(priv_key_bob, G, A, B, p)
# #
# # print("Alice's Public Key:", alice_public_key)
# # print("Bob's Public Key:", bob_public_key)

# class EllipticCurve:
#     """A simple Elliptic Curve class."""
#
#     def __init__(self, A, B, p):
#         self.A = A
#         self.B = B
#         self.p = p
#
#     def add(self, P, Q):
#         """Add two points P and Q on the elliptic curve."""
#         if P == (0, 0):
#             return Q
#         if Q == (0, 0):
#             return P
#         if P[0] == Q[0] and P[1] != Q[1]:
#             return (0, 0)  # Point at infinity
#
#         if P == Q:
#             lam = (3 * P[0]**2 + self.A) * pow(2 * P[1], -1, self.p) % self.p
#         else:
#             lam = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, self.p) % self.p
#
#         x3 = (lam**2 - P[0] - Q[0]) % self.p
#         y3 = (lam * (P[0] - x3) - P[1]) % self.p
#         return (x3, y3)
#
#     def scalar_mul(self, k, P):
#         """Multiply point P by scalar k on the elliptic curve."""
#         result = (0, 0)
#         while k:
#             if k & 1:
#                 result = self.add(result, P)
#             P = self.add(P, P)
#             k >>= 1
#         return result
#
# # Example usage
# A = 115792089210356248762697446949407573530086143415290314195533631308867097853948
# B = 41058363725152142129326129780047268409114441015993725554835256314039467401291
# p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
# G = (48439561293906451759052585252797914202762949526041747995844080717082404635286,
#      36134250956749795798585127919587881956611106672985015071877270311162452333045)
#
# curve = EllipticCurve(A, B, p)
#
# # Alice's and Bob's private keys
# Priv_Alice = 10007
# Priv_Bob = 97123
#
# # Calculate public keys
# alice_public_key = curve.scalar_mul(Priv_Alice, G)
# bob_public_key = curve.scalar_mul(Priv_Bob, G)
#
# print("Alice's Public Key:", alice_public_key)
# print("Bob's Public Key:", bob_public_key)
import hashlib
def mod_inverse(a, p):
    """Compute the modular inverse of a modulo p."""
    return pow(a, -1, p)

def elliptic_curve_addition(P, Q, A, p):
    """Perform addition on the elliptic curve."""
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P
    if P == Q:
        lam = (3 * P[0]**2 + A) * mod_inverse(2 * P[1], p) % p
    else:
        if P[0] == Q[0]:
            return (0, 0)  # Point at infinity
        lam = (Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p) % p

    x3 = (lam**2 - P[0] - Q[0]) % p
    y3 = (lam * (P[0] - x3) - P[1]) % p

    return (x3, y3)

def ecc_scalar_multiplication(k, G, A, p):
    """Perform scalar multiplication k*G on the elliptic curve."""
    result = (0, 0)  # Point at infinity
    addend = G

    while k:
        if k & 1:
            result = elliptic_curve_addition(result, addend, A, p)
        addend = elliptic_curve_addition(addend, addend, A, p)
        k >>= 1

    return result

# Elliptic curve parameters
# A = 2
# C = 24  # Note: Typically denoted as 'B' in y^2 = x^3 + Ax + B
A = 115792089210356248762697446949407573530086143415290314195533631308867097853948
C = 41058363725152142129326129780047268409114441015993725554835256314039467401291
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
G = (48439561293906451759052585252797914202762949526041747995844080717082404635286,
     36134250956749795798585127919587881956611106672985015071877270311162452333045)  # Generator point

# Alice's and Bob's secret keys
alice_secret = 10007
bob_secret = 97123

# Calculate public keys
alice_public = ecc_scalar_multiplication(alice_secret, G, A, p)
bob_public = ecc_scalar_multiplication(bob_secret, G, A, p)

# Calculate shared secrets
alice_shared_secret = ecc_scalar_multiplication(alice_secret, bob_public, A, p)
bob_shared_secret = ecc_scalar_multiplication(bob_secret, alice_public, A, p)

print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)
print("Alice's Shared Secret:", alice_shared_secret)
print("Bob's Shared Secret:", bob_shared_secret)

def point_to_bytes(point, p):
    """Convert a point into bytes."""
    x_bytes = point[0].to_bytes((p.bit_length() + 7) // 8, byteorder='big')
    y_bytes = point[1].to_bytes((p.bit_length() + 7) // 8, byteorder='big')
    return x_bytes + y_bytes

# Serialize the shared secrets to bytes
alice_shared_secret_bytes = point_to_bytes(alice_shared_secret, p)
bob_shared_secret_bytes = point_to_bytes(bob_shared_secret, p)

# Concatenate the serialized points
concatenated = alice_shared_secret_bytes + bob_shared_secret_bytes

# Calculate the session key using SHA3-256 hash
sha3_hash = hashlib.sha3_256(concatenated).digest()

# Convert the SHA3-256 hash to hexadecimal format
session_key_hex = sha3_hash.hex()
print('session_key_hex:', session_key_hex)


