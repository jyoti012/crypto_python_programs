import hashlib

def sha256_hash_hex_prefix(num, length=6):
    """ Return the first 'length' hex characters of the SHA-256 hash of the given number. """
    sha256_hash = hashlib.sha256(str(num).encode()).hexdigest()
    return sha256_hash[:length]

def find_matching_hash(target_num, hash_length=6):
    """ Find the lowest integer that has the same SHA-256 hash prefix as the target number. """
    target_hash_prefix = sha256_hash_hex_prefix(target_num, hash_length)
    i = 0
    while True:
        if sha256_hash_hex_prefix(i, hash_length) == target_hash_prefix:
            return i, target_hash_prefix
        i += 1

# Given integer
target_integer = 221123
matching_integer, hash_prefix = find_matching_hash(target_integer)

# Result
result = f"{matching_integer}:{hash_prefix}"
print(result)

