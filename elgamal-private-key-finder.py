from sympy import mod_inverse, isprime

def find_private_key(p, g, y):
    x = 1
    while x < p:
        if pow(g, x, p) == y:
            return x
        x += 1
    return None

def main():
    # Given public key (p, g, y)
    p = 99333611752778158313691997689669641978712476822507750499831812831584630785973  # Prime modulus
    g = 89590362417598127889763750591434581694337369135165007793050455118722836261003  # Generator
    y = 67931852888628538370037206937600742353104147135380482916521197699075937305150  # Public key

    # Calculate the private key (x) based on the provided information
    x = find_private_key(p, g, y)

    if x is not None:
        print(f"Private Key (x): {x}")
    else:
        print("Private key not found")

if __name__ == "__main__":
    main()
