# from sympy.ntheory.modular import solve_congruence
#
# def extended_gcd(a, b):
#     """ Extended Euclidean Algorithm """
#     if a == 0:
#         return b, 0, 1
#     gcd, x1, y1 = extended_gcd(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#     return gcd, x, y
#
# def modular_sqrt(a, p):
#     """ Find a modular square root of a mod p """
#     # Special case where p is a prime
#     if p % 4 == 3:
#         return pow(a, (p + 1) // 4, p)
#     else:
#         # Implementing Tonelli-Shanks algorithm or similar would be needed for other cases
#         raise NotImplementedError("The function is not implemented for primes where p % 4 != 3.")
#
# def chinese_remainder_theorem(a1, m1, a2, m2):
#     """ Chinese Remainder Theorem """
#     gcd, m1_inv, m2_inv = extended_gcd(m1, m2)
#     if gcd != 1:
#         raise ValueError("Moduli are not co-prime")
#     return (a1 * m2 * m2_inv + a2 * m1 * m1_inv) % (m1 * m2)
#
# # Given values
# N = 1933634525290622454540065264062502459106438695446778356749468846280140342570577537210036512734931880598023659304231738802513646204418925269099696441605428481281993294488022976327430363091028566393133679925891401994481785149172724022371935924551075909115454435898892409406084623706499466593848314912698405699824427259717082725088719907300864170959806751768147257
# C = 0x696c5289eaac71c3b047238e38e38e4
# p = 1390551877957199575037954793541476822970914083147535493229971480385161424944671571566805901143766166649018002569045512218416037631535638130144734364495362854115480267216524851908391
#
# # Calculate q
# q = N // p
#
# # Calculate the modular square roots
# m_p1 = modular_sqrt(C, p)
# m_p2 = p - m_p1
# m_q1 = modular_sqrt(C, q)
# m_q2 = q - m_q1
#
# # Apply the Chinese Remainder Theorem
# m1 = chinese_remainder_theorem(m_p1, p, m_q1, q)
# m2 = chinese_remainder_theorem(m_p1, p, m_q2, q)
# m3 = chinese_remainder_theorem(m_p2, p, m_q1, q)
# m4 = chinese_remainder_theorem(m_p2, p, m_q2, q)
#
# # Convert to hex format
# m_hex = [hex(m) for m in (m1, m2, m3, m4)]
# print(m_hex)


import gmpy2
N = 1933634525290622454540065264062502459106438695446778356749468846280140342570577537210036512734931880598023659304231738802513646204418925269099696441605428481281993294488022976327430363091028566393133679925891401994481785149172724022371935924551075909115454435898892409406084623706499466593848314912698405699824427259717082725088719907300864170959806751768147257
p=1390551877957199575037954793541476822970914083147535493229971480385161424944671571566805901143766166649018002569045512218416037631535638130144734364495362854115480267216524851908391

# p = 3860330774593352175517799374199641878898498526797023293185141540549370881554698222726574177727508601528805237406296759578412936096107831064081982637443316389782316750976195065604527
# C = 0x765a27fcc1123455794fa320fedcba99
C= 0x696c5289eaac71c3b047238e38e38e4

q = N // p

# Calculate r1, r2, r3, r4
r1 = gmpy2.powmod(C, (p + 1) // 4, N)
r2 = N - r1
r3 = gmpy2.powmod(C, (p + 1) // 4, p)
r4 = p - r3

# Check which root is correct
roots = [r1, r2, r3, r4]

for root in roots:
    if gmpy2.powmod(root, 2, N) == C:
        hex_key = hex(root)[2:]
        print("Recovered Hex Key:", hex_key)
        break