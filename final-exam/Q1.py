from typing import Tuple
BPolynomial = int
 
def p_mul(a: BPolynomial, b: BPolynomial) -> BPolynomial:
  """ Binary polynomial multiplication (peasant). """
  result = 0
  while a and b:
    if a & 1: result ^= b
    a >>= 1
    b <<= 1
  return result
 
def p_mod_inv(a: BPolynomial, modulus: BPolynomial) -> BPolynomial:
  """ Binary polynomial modular multiplicative inverse.
        Returns b so that: p_mod(p_mul(a, b), modulus) == 1
        Precondition: modulus != 0 and p_coprime(a, modulus)
        Postcondition: b < modulus """
  d, x, y = p_egcd(a, modulus)
  assert d == 1  # inverse exists
  return x
 
def p_egcd(a: BPolynomial,
           b: BPolynomial) -> tuple[BPolynomial, BPolynomial, BPolynomial]:
  """ Binary polynomial Extended Euclidean algorithm (iterative).
        Returns (d, x, y) where d is the Greatest Common Divisor of polynomials a and b.
        x, y are polynomials that satisfy: p_mul(a,x) ^ p_mul(b,y) = d
        Precondition: b != 0
        Postcondition: x <= p_div(b,d) and y <= p_div(a,d) """
  a = (a, 1, 0)
  b = (b, 0, 1)
  while True:
    q, r = p_divmod(a[0], b[0])
    if not r: return b
    a, b = b, (r, a[1] ^ p_mul(q, b[1]), a[2] ^ p_mul(q, b[2]))
 
def p_divmod(a: BPolynomial,
             b: BPolynomial) -> Tuple[BPolynomial, BPolynomial]:
  """ Binary polynomial division.
        Divides a by b and returns resulting (quotient, remainder) polynomials.
        Precondition: b != 0 """
  q = 0
  bl = b.bit_length()
  while True:
    shift = a.bit_length() - bl
    if shift < 0: return (q, a)
    q ^= 1 << shift
    a ^= b << shift
binary_a = 0b1111000100000000011001011101101100110110011010011110110100000000000000100011111111001010100001000000111001001101010011101110111111011000100111111010001010000000001010000001010111111000100110011010001001101010001100011000001011000010001000100101011000001100
binary_m = 0b10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011111101111
decimal_number = p_mod_inv(binary_a, binary_m)
print('hexadecimal value - ', hex(decimal_number))