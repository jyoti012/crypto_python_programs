from hashlib import sha3_256
import random
from Crypto.Hash import SHA3_256

def keccak_sha3_256_hash_point(point):
	"""Calculate the KECCAK SHA3-256 hash of an elliptic curve point."""
	# Concatenate the x and y coordinates into a single string
	input_data = f"{point[0]}{point[1]}".encode()

	# Compute the hash
	hasher = SHA3_256.new()
	hasher.update(input_data)
	return int(hasher.hexdigest(), 16)


# Example of using the function
# point = (431569254910516832427588218486, 552372884790064035502657443372)
# point_hash = keccak_sha3_256_hash_point(point)
# print(point_hash)

# Elliptic Curve Parameters
A = 431716964419619625852480136574
B = 411179566297298325237704143111
P = 1072492247682744227234349329021
N = 153213178240392022988653913160
G = (947861218431381305431186994492, 647869014236366115537544007004)

# Point Q (Public Key)
Q = (102358487128865733008953462445, 810860435585488060357471027194)

# Private Key
private_key = 74747904694312937207160092918

# Plaintext (DES Key)
plaintext_hex = "AA:AA:AA:AA:AA:AA:AA:AA"
plaintext = int(plaintext_hex.replace(":", ""), 16)


# Function Definitions (elliptic_curve_add, elliptic_curve_multiply, keccak_sha3_256, etc.)
def elliptic_curve_add(P1, P2):
	if P1 == P2:
		lam = (3 * P1[0] ** 2 + A) * pow(2 * P1[1], -1, P)
	else:
		lam = (P2[1] - P1[1]) * pow(P2[0] - P1[0], -1, P)
	x3 = (lam ** 2 - P1[0] - P2[0]) % P
	y3 = (lam * (P1[0] - x3) - P1[1]) % P
	return x3, y3


def elliptic_curve_multiply(P, k):
	result = None
	addend = P

	for bit in reversed(bin(k)[2:]):
		if bit == '1':
			result = elliptic_curve_add(result, addend) if result else addend
		addend = elliptic_curve_add(addend, addend)

	return result


def keccak_sha3_256_hash(input_data):
	hasher = sha3_256()
	hasher.update(input_data.to_bytes((input_data.bit_length() + 7) // 8, byteorder='big'))
	return int.from_bytes(hasher.digest(), byteorder='big') % P


# Encryption
def eceg_encrypt(G, Q, plaintext):
	k = random.randint(1, N - 1)
	kG = elliptic_curve_multiply(G, k)
	kQ = elliptic_curve_multiply(Q, k)
	hashed_kQ = keccak_sha3_256_hash_point(kQ)
	cipher = (kG, (plaintext + hashed_kQ) % P)
	return cipher

# Decryption
def eceg_decrypt(cipher, private_key):
	kG, y2 = cipher
	s_kG = elliptic_curve_multiply(kG, private_key)
	hashed_s_kG = keccak_sha3_256_hash_point(s_kG)
	decrypted_text = (y2 - hashed_s_kG) % P
	return decrypted_text


# Perform Encryption
cipher = eceg_encrypt(G, Q, plaintext)

# Perform Decryption
decrypted_text = eceg_decrypt(cipher, private_key)

# Convert decrypted text back to hex format
decrypted_text_hex = format(decrypted_text, 'x').upper()
decrypted_text_formatted = ":".join(decrypted_text_hex[i:i + 2] for i in range(0, len(decrypted_text_hex), 2))

print("Encrypted Ciphertext:", cipher)
print("Decrypted Text:", decrypted_text_formatted)
