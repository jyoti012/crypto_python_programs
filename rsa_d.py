from math import gcd


def find_gcd(num1, num2):
	"""Method to find the greatest common divisor (GCD) of two numbers"""
	return gcd(num1, num2)


def main():
	# Variable declarations
	plaintext = "127458934542242345565645767"
	print("Original Message is:", plaintext)
	msg = int(plaintext)

	# Variables for prime numbers and calculations
	input1 = "10092003300140014003"  # First prime number
	input2 = "975319753197531975319"  # Second prime number

	# Step 1: Initialize prime numbers p and q
	p = int(input1)
	q = int(input2)

	# Step 2: Calculate n = p * q (Modulus for public and private keys)
	n = p * q
	print('n = ', n)
	# Step 3: Calculate Euler's totient function ϕ(n) = (p - 1) * (q - 1)
	z = (p - 1) * (q - 1)
	print("the value of ϕ(n) =", z)  # Printing the value of ϕ(n)

	# Step 4: Find public key exponent e
	for e in range(2, z + 1):
		if find_gcd(e, z) == 1:
			break
	print("the value of e =", e)  # e is part of the public key

	# Step 5: Calculate private key exponent d
	d = 0
	for i in range(10):
		x = 1 + z * i  # x = 1 + i * z
		if x % e == 0:
			d = x // e  # Calculating d
			break
	print("the value of d =", d)  # d is part of the private key

	# Encrypting the message
	c = pow(msg, e, n)
	print("Encrypted message is:", c)

	# Decrypting the message
	msgback = pow(c, d, n)
	print("Decrypted message is:", msgback)


if __name__ == "__main__":
	main()
