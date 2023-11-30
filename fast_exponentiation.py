

def fast_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result = (result * base) % modulus
        exponent = exponent // 2  # Divide the exponent by 2
        base = (base * base) % modulus

    return result

# Example RSA setup
p = 10092003300140014003
q = 975319753197531975319
n = p * q
phi_n = (p - 1) * (q - 1)
e = 5  # public exponent
d = 7874344134368989334911690638229790722109  # private exponent

# Example message
M = 127458934542242345565645767

# Encrypting the message
C = fast_exponentiation(M, e, n)
print("Encrypted message:", C)

# Decrypting the message
M_decrypted = fast_exponentiation(C, d, n)
print("Decrypted message:", M_decrypted)
