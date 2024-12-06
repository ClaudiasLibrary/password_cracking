# utils.py
import hashlib
import bcrypt
import itertools
import string

def crack_md5_hash(hash_string, wordlist):
    """ Crack MD5 hashes using a dictionary attack. """
    with open(wordlist, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if hashlib.md5(word.encode('utf-8')).hexdigest() == hash_string:
                return word
    return None

def crack_sha1_hash(hash_string, wordlist):
    """ Crack SHA1 hashes using a dictionary attack. """
    with open(wordlist, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if hashlib.sha1(word.encode('utf-8')).hexdigest() == hash_string:
                return word
    return None

def crack_sha256_hash(hash_string, wordlist):
    """ Crack SHA256 hashes using a dictionary attack. """
    with open(wordlist, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if hashlib.sha256(word.encode('utf-8')).hexdigest() == hash_string:
                return word
    return None

def crack_bcrypt_hash(hash_string, wordlist):
    """ Crack bcrypt hashes using a dictionary attack. """
    with open(wordlist, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if bcrypt.checkpw(word.encode('utf-8'), hash_string.encode('utf-8')):
                return word
    return None

def brute_force_crack(hash_string, algorithm, max_len=4):
    """ Attempt brute force cracking (only for weak hashes like MD5 and SHA1). """
    charset = string.ascii_lowercase + string.digits
    attempts = 0
    for length in range(1, max_len+1):
        for password in itertools.product(charset, repeat=length):
            password = ''.join(password)
            attempts += 1
            if algorithm == "md5" and hashlib.md5(password.encode('utf-8')).hexdigest() == hash_string:
                return password, attempts
            elif algorithm == "sha1" and hashlib.sha1(password.encode('utf-8')).hexdigest() == hash_string:
                return password, attempts
    return None, attempts
