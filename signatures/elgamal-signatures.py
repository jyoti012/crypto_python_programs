from hashlib import sha256
from Crypto.Util.number import inverse, GCD
import random
from sympy.ntheory import factorint


# ElGamal Signature Generation Function
def elgamal_sign(m, p, g, x):
	"""
	m: original message
	p: large prime number
	g: primitive root modulo p
	x: private key
	"""
	# Hash the message
	h = int(sha256(m.encode('utf-8')).hexdigest(), 16)

	# Choose random k coprime to (p-1)
	while True:
		k = random.randint(1, p - 2)
		if GCD(k, p - 1) == 1:
			break

	# Calculate a = g^k mod p
	a = pow(g, k, p)

	# Calculate b = (h - x*a) * k^-1 mod (p-1)
	b = ((h - x * a) * inverse(k, p - 1)) % (p - 1)

	return a, b


# ElGamal Signature Verification Function
def elgamal_verify(m, a, b, p, g, y):
	"""
	m: original message
	a, b: signature components
	p: large prime number
	g: primitive root modulo p
	y: public key
	"""
	# Hash the message
	h = int(sha256(m.encode('utf-8')).hexdigest(), 16)

	# Verify the signature
	v1 = pow(g, h, p)
	v2 = (pow(y, a, p) * pow(a, b, p)) % p

	return v1 == v2


# Parameters for demonstration (not secure)
p = 23
x = 6  # Private key (x < p)


# Function to find a primitive root modulo p
def find_primitive_root(primitive_root):  # Primitive root mod p
	factors = list(factorint(primitive_root - 1).keys())  # Find prime factors of p-1

	for g in range(2, primitive_root):  # Test each candidate g from 2 to p-1
		if all(pow(g, (primitive_root - 1) // factor, primitive_root) != 1 for factor in factors):
			return g  # If condition holds for all factors, g is a primitive root
	return None  # If no primitive root is found


g = find_primitive_root(p)
print(f'Primitive root modulo g: {g}')

# Calculate public key
y = pow(g, x, p)

# Message to be signed
message = "This is a test message."

# Generate signature
signature = elgamal_sign(message, p, g, x)
print(f'Signature: {signature}')

# Verify signature
is_valid = elgamal_verify(message, signature[0], signature[1], p, g, y)
print(f'Signature valid: {is_valid}')
