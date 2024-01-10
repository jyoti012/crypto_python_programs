from sympy.ntheory.modular import solve_congruence

# Given partial keys (mi:ai)
congruences = [(705, 991), (760, 1009), (651, 691), (664, 811), (62, 877)]

# Solving the congruences using CRT
full_key = solve_congruence(*congruences)
print(full_key)
