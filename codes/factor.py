# import gmpy2
#
# def fermat(n):
#     tries = 1000000000000
#     a = gmpy2.isqrt(n)
#     c = 0
#
#     while not gmpy2.is_square(a**2 - n):
#         a += 1
#         c += 1
#
#         if c > tries:
#             return False
#
#     bsq = a**2 - n
#     b = gmpy2.isqrt(bsq)
#     p = a + b
#     q = a - b
#
#     return [p, q]
#
# print(fermat(16388146785521859419328389697421477502048096419704862847263007693464999236299623921516567811941373667059038257106166917278441193310601099360397641451666856858705465593894371504824507056285972019017595598902435357260719171905894720407727146325756281473246660334396380531230873912665633815745314899191842569807066612318889127278374342586156013615158934592022778730974305363604854229510012969372261879259614819305977892023909
# ))
# print(fermat(1050589))

# import gmpy2
#
# def fermat(n):
#     max_tries = 1000000000000  # Maximum number of tries
#     a = gmpy2.isqrt(n)
#     c = 0
#
#     while not gmpy2.is_square(a**2 - n):
#         a += 1
#         c += 1
#
#         if c > max_tries:
#             return None, None, c  # Return factors as None and the number of tries
#
#     bsq = a**2 - n
#     b = gmpy2.isqrt(bsq)
#     p = a + b
#     q = a - b
#
#     return p, q, c
#
# # Example usage:
# n = 16388146785521859419328389697421477502048096419704862847263007693464999236299623921516567811941373667059038257106166917278441193310601099360397641451666856858705465593894371504824507056285972019017595598902435357260719171905894720407727146325756281473246660334396380531230873912665633815745314899191842569807066612318889127278374342586156013615158934592022778730974305363604854229510012969372261879259614819305977892023909
# factors_p, factors_q, num_tries = fermat(n)
#
# print("Factor 1 (p):", factors_p)
# print("Factor 2 (q):", factors_q)
# print("Factors not found within", num_tries, "tries")

import gmpy2
import time

def fermat(n):
    max_tries = 1000000000000  # Maximum number of tries
    a = gmpy2.isqrt(n)
    c = 0

    start_time = time.time()  # Record the start time

    while not gmpy2.is_square(a**2 - n):
        a += 1
        c += 1

        if c > max_tries:
            end_time = time.time()  # Record the end time
            elapsed_time = end_time - start_time
            return None, None, c, elapsed_time  # Return factors as None, tries, and elapsed time

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time

    bsq = a**2 - n
    b = gmpy2.isqrt(bsq)
    p = a + b
    q = a - b

    return p, q, c, elapsed_time

# Example usage:
n = 25167873716576800554031364443594764006792378425391195653877657451465085654239628336275599853259118798126811320565317417275284820008706538000037323831866052656892703725867107090420670418920683447224453822205995473545258760298102718429422980877314329062078094056821524392122703277668966308297219057341700329141
factors_p, factors_q, num_tries, elapsed_time = fermat(n)

if factors_p and factors_q:
    print("Factor 1 (p):", factors_p)
    print("Factor 2 (q):", factors_q)
    print("Factors found in", num_tries, "tries")
    print("Elapsed time:", elapsed_time, "seconds")
else:
    print("Factors not found within", num_tries, "tries")
