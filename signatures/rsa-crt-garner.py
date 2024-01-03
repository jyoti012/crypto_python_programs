# Example from the pdf

p = 37
q = 10007
n = 370259  # n is the product of p and q
Sp = 27
Sq = 8102

# Python's pow function can be used to calculate modular inverse
p_inv_mod_q = pow(p, -1, q)  # p inverse mod q

# Apply Garner's formula to combine Sp and Sq into S
S = (Sp + p * p_inv_mod_q * ((Sq - Sp) % n)) % n
print('Signature: ', S)

# Given public key (e, n) and signature S
e = 265097

# Given hash of the message h(M)
h_M = 11

# Verify the signature
# Compute S^e mod n and check if it matches h(M)
verified = pow(S, e, n) == h_M
print('Verify signature: ', verified)

# Calculate Sp and Sq

# Given values
p1 = 37
q1 = 10007
h1 = 11  # hash of the message
n1 = p1 * q1  # n is the product of p and q

# Assuming d is the private key exponent. In actual RSA,
# d is calculated from e, p, and q, but it's not provided here.
# As d is not given, we will use a demonstration value for d.
# This is just for demonstration and not actual RSA calculation.
d_demo = 9090  # This is a placeholder value for demonstration

# Calculate Sp and Sq
Sp1 = pow(h1, d_demo, p)
Sq1 = pow(h1, d_demo, q)

print('Sp: ', Sp, 'Sq: ', Sq)


