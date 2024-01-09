class EllipticCurveGeneric:
    """
    A simple class to represent an Elliptic Curve over a finite field for generic curves.
    Curve equation: y^2 = x^3 + ax + b
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
            return (0, 0)  # Point at infinity
        if P != Q:
            m = (Q[1] - P[1]) * self.inverse_mod(Q[0] - P[0], self.p) % self.p
        else:
            m = (3 * P[0]**2 + self.a) * self.inverse_mod(2 * P[1], self.p) % self.p
        x = (m**2 - P[0] - Q[0]) % self.p
        y = (m * (P[0] - x) - P[1]) % self.p
        return (x, y)

    def mul(self, P, n):
        R = (0, 0)  # Identity element (point at infinity)
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
        return ud % m

def ecdsa_verify_with_curve(h, r, s, curve, P, Y, q):
    w = curve.inverse_mod(s, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    V = curve.add(curve.mul(P, u1), curve.mul(Y, u2))
    return V[0] % q == r

# Given parameters
p = 17   # Field prime
curve = EllipticCurveGeneric(a=2, b=2, p=p)  # Elliptic curve y^2 = x^3 + 2x + 2
q = 19   # Order of the curve
P = (5, 1) # Base point
Y = (0, 6) # Public key
h = 26   # Hash of the message
r, s = (9, 17) # Signature

# Verify the signature using the provided curve
verification_result = ecdsa_verify_with_curve(h, r, s, curve, P, Y, q)
print("Verification Result:", verification_result)
