from hashlib import sha3_256
import random

# Elliptic Curve Parameters
A = 431716964419619625852480136574
B = 411179566297298325237704143111
P = 1072492247682744227234349329021
N = 153213178240392022988653913160
G = (947861218431381305431186994492, 647869014236366115537544007004)


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


def eceg_encrypt(public_key, plaintext):
	k = random.randint(1, N)
	kG = elliptic_curve_multiply(G, k)
	kQ = elliptic_curve_multiply(public_key, k)
	hashed_kQ = keccak_sha3_256_hash(int(f"{kQ[0]}{kQ[1]}"))
	y2 = (plaintext + hashed_kQ) % P
	return (*kG, y2)


def eceg_decrypt(private_key, cipher):
	kG = (cipher[0], cipher[1])
	y2 = cipher[2]
	s_kG = elliptic_curve_multiply(kG, private_key)
	hashed_s_kG = keccak_sha3_256_hash(int(f"{s_kG[0]}{s_kG[1]}"))
	return (y2 - hashed_s_kG) % P


def format_as_hex_string(value):
	""" Format a number as a hex string in the format 'XX:XX:XX:XX:XX:XX:XX:XX'. """
	hex_str = format(value, '016x')  # Convert to hex string, padded to 16 characters
	return ':'.join(hex_str[i:i + 2] for i in range(0, len(hex_str), 2))


# Main function
def main():
	# Convert plaintext (DES key) to BigInteger
	plaintext = int("AAAAAAAAAAAAAAAA", 16)

	# Key generation
	private_key = random.randint(1, N)
	public_key = elliptic_curve_multiply(G, private_key)

	# Encryption
	cipher = eceg_encrypt(public_key, plaintext)
	print("cipher Text:", cipher)

	# Decryption
	decrypted_text = eceg_decrypt(private_key, cipher)

	print("Original Plaintext:", plaintext)
	print("Decrypted Text:", decrypted_text)

	# Formatting results in hex format separated by ':'
	formatted_plaintext = format_as_hex_string(plaintext)
	formatted_decrypted_text = format_as_hex_string(decrypted_text)

	print("Original Plaintext:", formatted_plaintext)
	print("Decrypted Text:", formatted_decrypted_text)


if __name__ == "__main__":
	main()
