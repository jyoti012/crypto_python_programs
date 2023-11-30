from sympy.abc import x, y
from sympy import Eq, mod_inverse, solve

def elliptic_curve_addition(P, Q, A, p):
    """Perform addition on the elliptic curve."""
    if P == Q:  # Doubling
        slope = (3 * P[0]**2 + A) * mod_inverse(2 * P[1], p) % p
    else:  # Point addition
        slope = (Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p) % p

    x3 = (slope**2 - P[0] - Q[0]) % p
    y3 = (slope * (P[0] - x3) - P[1]) % p

    return (x3, y3)

def elliptic_curve_multiply(P, k, A, p):
    """Perform scalar multiplication on the elliptic curve."""
    R = P
    for _ in range(k - 1):
        R = elliptic_curve_addition(R, P, A, p)
    return R

def simple_hash(point):
    """A simple hash function for demonstration."""
    return (point[0] + point[1]) % 11

# Elliptic curve: y^2 = x^3 + x + 6 mod 11
A, B, p = 1, 6, 11

# Setup
P = (2, 7)  # Point on the curve
s = 7  # Private key
Q = elliptic_curve_multiply(P, s, A, p)  # Public key

# Example values
m = 9  # Message
k = 6  # Random integer

# Encryption
kP = elliptic_curve_multiply(P, k, A, p)
kQ = elliptic_curve_multiply(Q, k, A, p)
H_kQ = simple_hash(kQ)  # Simple hash function
y1 = kP  # Point compression not implemented, using kP directly
y2 = (m + H_kQ) % p

# Decryption
R = elliptic_curve_multiply(y1, s, A, p)
H_R = simple_hash(R)
m_decrypted = (y2 - H_R) % p

print(y1, y2, m_decrypted)

