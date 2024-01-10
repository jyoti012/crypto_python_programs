from sympy import mod_inverse

# Euler totient function to calculate private key d
def compute_private_key(n, e):
    # Step 1: Factor n into p and q
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            break

    # Step 2: Compute φ(n)
    phi_n = (p - 1) * (q - 1)

    # Step 3: Compute the private key d
    d = mod_inverse(e, phi_n)

    return d

# Given RSA parameters
n = 217891
e = 101

# Compute the private key
d = compute_private_key(n, e)
print("Private key d:", d)
