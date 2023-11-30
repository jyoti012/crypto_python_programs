def fast_exponentiation(a, b, n):
	t = 1  # Initialize result

	# Loop until b becomes zero
	while b != 0:
		# If b is odd, multiply t with the current a and take mod n
		if b % 2 == 1:
			t = (t * a) % n

		# Shift b to right by 1 (equivalent to floor division by 2)
		b = b // 2

		# Square a and take mod n
		a = (a * a) % n

	# Return the result
	return t


# Read a, b, n (example values)
a = 987654321
b = 123456789
n = 1000000007

# Calculate a^b mod n
result = fast_exponentiation(a, b, n)
print('a^b mod n = ', result)
