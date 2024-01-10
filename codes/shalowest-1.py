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

def find_alternate_matching_hash(target_num, hash_length=6):
    """ Find an alternate integer (other than the target) that has the same SHA-256 hash prefix. """
    target_hash_prefix = sha256_hash_hex_prefix(target_num, hash_length)
    i = 0
    while True:
        if i != target_num:
            if sha256_hash_hex_prefix(i, hash_length) == target_hash_prefix:
                return i, target_hash_prefix
        i += 1

# Given integer
target_integer = 221123

# Finding the matching hash
matching_integer, hash_prefix = find_matching_hash(target_integer)

# Finding the alternate matching hash
alternate_matching_integer, hash_prefix = find_alternate_matching_hash(target_integer)

# Results
result = f"{matching_integer}:{hash_prefix}"
alternate_result = f"{alternate_matching_integer}:{hash_prefix}"

print(result, alternate_result)
