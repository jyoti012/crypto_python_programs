import math


def calculate_d(e, phi_n):
	# Extended Euclidean Algorithm to find the modular inverse
	d, x1, x2, y1 = 0, 0, 1, 1
	original_phi_n = phi_n

	while e > 1:
		# Quotient
		q = e // phi_n

		# Remainder
		t = phi_n

		# Update phi_n
		phi_n = e % phi_n
		e = t
		t = x1

		# Update x1 and x2
		x1 = x2 - q * x1
		x2 = t

	# Make x2 positive
	if x2 < 0:
		x2 = x2 + original_phi_n

	return x2


def fermat_factorization(n):
	t = math.ceil(math.sqrt(n))
	while True:
		s_square = t ** 2 - n
		if s_square >= 0:
			s = math.sqrt(s_square)
			if s.is_integer():
				return (t + int(s), t - int(s))
		t += 1


# Given values
# e = 708473
# n = 1050589

# Factorizing n to find p and q
# p, q = fermat_factorization(n)
p = 7
q = 17
e = 5
n = p * q
# Calculate phi(n)
phi_n = (p - 1) * (q - 1)

# Calculate d
d = calculate_d(e, phi_n)
print('d = ', d)

# Public Key (e, n)
print('Public Key (e, n) = ', (e, n))
# Private Key (d,n)
print('Private Key (d,n)', (d, n))

# Given composite number 'n' to factor
n1 = 1050589


# Function to perform Fermat's factorization
def fermat_factorization_1(n):
	s = int(math.isqrt(n))  # Initialize s as the integer square root of n

	while True:
		t_squared = s * s - n  # Calculate t^2 - n

		if t_squared >= 0:
			t = int(math.isqrt(t_squared))  # Calculate the square root of t_squared

			if t * t == t_squared:
				p = s + t
				q = s - t
				return p, q

		s += 1  # Increment s and continue


# Perform Fermat's factorization
p, q = fermat_factorization_1(n1)

print("Factor 1 (p):", p)
print("Factor 2 (q):", q)
