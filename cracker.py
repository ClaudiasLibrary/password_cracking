# cracker.py
import time
from utils import crack_md5_hash, crack_sha1_hash, crack_sha256_hash, crack_bcrypt_hash, brute_force_crack
from hash_identification import identify_hash
from config import WORDLIST_PATH, OUTPUT_REPORT


def run_cracking(hash_string):
    hash_type = identify_hash(hash_string)
    print(f"Identified hash type: {hash_type}")

    if hash_type == "md5":
        result = crack_md5_hash(hash_string, WORDLIST_PATH)
    elif hash_type == "sha1":
        result = crack_sha1_hash(hash_string, WORDLIST_PATH)
    elif hash_type == "sha256":
        result = crack_sha256_hash(hash_string, WORDLIST_PATH)
    elif hash_type == "bcrypt":
        result = crack_bcrypt_hash(hash_string, WORDLIST_PATH)
    else:
        print("Unknown hash type.")
        return None

    if result:
        print(f"Password cracked: {result}")
    else:
        print("Hash not cracked using the dictionary. Attempting brute-force...")
        result, attempts = brute_force_crack(hash_string, hash_type)
        if result:
            print(f"Brute-force success: {result} after {attempts} attempts.")
        else:
            print("Brute-force failed to crack the hash.")

    return result


def generate_report(hash_string, cracked_password, hash_type):
    with open(OUTPUT_REPORT, 'w') as file:
        file.write("<html><head><title>Hash Cracking Report</title></head><body>")
        file.write(f"<h1>Hash Cracking Report</h1>")
        file.write(f"<h2>Hash: {hash_string}</h2>")
        file.write(f"<h2>Hash Type: {hash_type}</h2>")
        if cracked_password:
            file.write(f"<p><b>Cracked Password: </b>{cracked_password}</p>")
        else:
            file.write("<p>Password not cracked.</p>")
        file.write("</body></html>")


if __name__ == "__main__":
    hash_to_crack = input("Enter hash to crack: ")
    start_time = time.time()
    cracked_password = run_cracking(hash_to_crack)
    end_time = time.time()
    hash_type = identify_hash(hash_to_crack)
    generate_report(hash_to_crack, cracked_password, hash_type)
    print(f"Cracking completed in {end_time - start_time:.2f} seconds.")
