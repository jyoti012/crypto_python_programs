import math


def fermat_factorization(n):
	t = math.ceil(math.sqrt(n))
	while True:
		s_square = t ** 2 - n
		if s_square >= 0:
			s = math.sqrt(s_square)
			if s.is_integer():
				return (t + int(s), t - int(s))
		t += 1


# Given n
n = 1050589

# Finding p and q using Fermat's factorization method
p, q = fermat_factorization(n)
print('n = ', n)
print('p = ', p, 'q = ', q)
