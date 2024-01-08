from sympy import mod_inverse
# def mod_inverse(a, m):
#     """Compute the modular inverse of a modulo m."""
#     return pow(a, -1, m)

def elliptic_curve_addition(P, Q, A, p):
    """Perform addition on the elliptic curve."""
    if P == Q:  # Doubling
        slope = (3 * P[0]**2 + A) * mod_inverse(2 * P[1], p) % p
    else:  # Point addition
        slope = (Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p) % p

    x3 = (slope**2 - P[0] - Q[0]) % p
    y3 = (slope * (P[0] - x3) - P[1]) % p

    return (x3, y3)

def ecc_scalar_multiplication(k, G, A, B, p):
    """Perform scalar multiplication k*G on an elliptic curve."""
    result = G
    for _ in range(k - 1):
        result = elliptic_curve_addition(result, G, A, p)
    return result

# Example usage
A = 115792089210356248762697446949407573530086143415290314195533631308867097853948
B = 41058363725152142129326129780047268409114441015993725554835256314039467401291
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
G = (48439561293906451759052585252797914202762949526041747995844080717082404635286,
     36134250956749795798585127919587881956611106672985015071877270311162452333045)

# Alice's and Bob's private keys
priv_key_alice = 10007
priv_key_bob = 97123

# Calculate public keys
alice_public_key = ecc_scalar_multiplication(priv_key_alice, G, A, B, p)
bob_public_key = ecc_scalar_multiplication(priv_key_bob, G, A, B, p)

print("Alice's Public Key:", alice_public_key)
print("Bob's Public Key:", bob_public_key)

#
# # Curve parameters
# A = 115792089210356248762697446949407573530086143415290314195533631308867097853948
# B = 41058363725152142129326129780047268409114441015993725554835256314039467401291
# p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
#
# # Generator point G
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
