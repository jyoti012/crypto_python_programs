from Crypto.Util.number import getPrime
from random import randint

# ElGamal Key Generation
# public key = (p,g,y)
# private key = x
# message = m
# k = random random integer such that 1<k<p−1
# g = a number less than p which, when raised to successive powers,
# generates a large subset of the elements in the group
def generate_elgamal_keypair(keysize):
	# Generate a large prime number p
	# p = getPrime(keysize)
	# Select a generator g
	# g = randint(2, p - 2)
	# Choose a private key x
	# x = randint(1, p - 2)
	# Compute the public key y
	p=1009
	x=237
	g=101
	y = pow(g, x, p)

	return (p, g, y), x


# ElGamal Encryption
def elgamal_encrypt(public_key, message):
	p, g, y = public_key

	if not (0 < message < p):
		raise ValueError("Message must be an integer less than p.")

	# k = randint(1, p - 1)
	k= 291 # k = random number
	c1 = pow(g, k, p)
	c2 = (message * pow(y, k, p)) % p

	return c1, c2


# ElGamal Decryption
def elgamal_decrypt(private_key, cipher_text, p):
	c1, c2 = cipher_text
	s = pow(c1, private_key, p)
	m = (c2 * pow(s, p - 2, p)) % p  # Using Fermat's Little Theorem for modular inverse
	return m


# Example usage
# Generate keys
keysize = 2048  # Key size (in bits)
public_key, private_key = generate_elgamal_keypair(keysize)
message = 559  # Example message
# Encrypt a message
print("Original message m = ", message)
cipher_text = elgamal_encrypt(public_key, message)
print("Encrypted message:", cipher_text)

# Decrypt the message
decrypted_message = elgamal_decrypt(private_key, cipher_text, public_key[0])
print("Decrypted message:", decrypted_message)
