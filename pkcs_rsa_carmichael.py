from sympy import lcm, isprime
from random import randrange
from math import gcd
from sympy import mod_inverse

# The private key d in RSA is the modular multiplicative inverse of
# e modulo ϕ(n) (or) λ(n)). The choice between
# ϕ(n) and λ(n) can result in different values for d,
# although both are mathematically valid for decryption in RSA.
def generate_prime_candidate(length):
	# Generate a random odd integer
	p = randrange(2 ** (length - 1), 2 ** length)
	return p | 1  # ensure it's odd

def find_prime(length=10):
	p = 4
	# Keep generating until a prime is found
	while not isprime(p):
		p = generate_prime_candidate(length)
	return p


def rsa_key_generation():
	# Step 1: Select two prime numbers
	# p = find_prime()
	# q = find_prime()
	p = 1999
	q = 109
	while q == p:
		q = find_prime()

	# Step 2: Calculate n and λ(n)
	n = p * q
	lambda_n = lcm(p - 1, q - 1)

	# Step 3: Choose e
	e = 101
	while gcd(e, lambda_n) != 1:
		e += 2

	# Step 4: Calculate d
	d = mod_inverse(e, lambda_n)

	return (e, n), (d, n)


# Example usage
public_key, private_key = rsa_key_generation()
print("Public Key: ", public_key)
print("Private Key: ", private_key)
