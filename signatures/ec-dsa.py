from ecdsa import SigningKey, NIST384p


def sign_message(message):
	"""Sign a message using ECDSA."""
	# Generate a private key for signing
	private_key = SigningKey.generate(curve=NIST384p)

	# Sign the message
	signature = private_key.sign(message.encode())

	# Return the signature and the private key's public key for verification
	return signature, private_key.get_verifying_key()


def verify_signature(message, signature, public_key):
	"""Verify a message's signature using ECDSA."""
	try:
		# Verify the signature
		return public_key.verify(signature, message.encode())
	except:
		# If verification fails, return False
		return False


# Example usage
message = "Hello, this is a test message."

# Signing the message
signature, public_key = sign_message(message)
print("Signature:", signature)

# Verifying the signature
verification_result = verify_signature(message, signature, public_key)
print("Verification Result:", verification_result)
