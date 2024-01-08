class EllipticCurve:
    """
    A simple class to represent an Elliptic Curve over a finite field.
    """
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def add(self, P, Q):
        if P == (0, 0):
            return Q
        if Q == (0, 0):
            return P
        if P[0] == Q[0] and (P[1] != Q[1] or P[1] == 0):
            return (0, 0)
        if P != Q:
            m = (Q[1] - P[1]) * self.inverse_mod(Q[0] - P[0], self.p) % self.p
        else:
            m = (3 * P[0]**2 + self.a) * self.inverse_mod(2 * P[1], self.p) % self.p
        x = (m**2 - P[0] - Q[0]) % self.p
        y = (m * (P[0] - x) - P[1]) % self.p
        return (x, y)

    def mul(self, P, n):
        R = (0, 0) # The identity element (point at infinity)
        while n > 0:
            if n & 1 == 1:
                R = self.add(R, P)
            P = self.add(P, P)
            n >>= 1
        return R

    def inverse_mod(self, a, m):
        if a < 0 or m <= a:
            a = a % m
        c, d = a, m
        uc, vc, ud, vd = 1, 0, 0, 1
        while c != 0:
            q, c, d = divmod(d, c) + (c,)
            uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc
        if d == 1:
            return ud % m
        raise Exception('inverse_mod: no inverse exists')

def ecdsa_sign(h, x, k, curve, P, q):
    R = curve.mul(P, k)
    r = R[0] % q
    s = ((h + x*r) * curve.inverse_mod(k, q)) % q
    return r, s

def ecdsa_verify(h, r, s, curve, P, Y, q):
    w = curve.inverse_mod(s, q)
    a = (h * w) % q
    b = (r * w) % q
    V = curve.add(curve.mul(P, a), curve.mul(Y, b))
    return V[0] % q == r

# Define the elliptic curve y^2 = x^3 + x + 3 over F_199
curve = EllipticCurve(a=1, b=3, p=199)

# Given parameters
P = (1, 76)  # Base point
q = 197      # Order of the curve
x = 29       # Private key
Y = (113, 191) # Public key
h = 68       # Hash of the message
k = 153      # Per-message secret number

# Sign the message
r, s = ecdsa_sign(h, x, k, curve, P, q)
print("Signature (r, s):", r, s)

# Verify the signature
verification_result = ecdsa_verify(h, r, s, curve, P, Y, q)
print("Verification Result:", verification_result)
