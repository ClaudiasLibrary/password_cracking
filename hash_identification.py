# hash_identification.py

def identify_hash(hash_string):
    """ Identify the hash algorithm used in the given hash string. """
    if len(hash_string) == 32:
        try:
            int(hash_string, 16)  # MD5 hashes are 32 characters long and hexadecimal
            return "md5"
        except ValueError:
            pass
    elif len(hash_string) == 40:
        return "sha1"
    elif len(hash_string) == 64:
        return "sha256"
    elif len(hash_string) == 60 and hash_string.startswith('$2b$'):
        return "bcrypt"
    return "unknown"

def is_salted(hash_string):
    """ Check if the hash is salted (e.g., bcrypt hashes typically contain a salt). """
    if hash_string.startswith('$2b$'):
        return True
    return False
