# Automated Password Cracking and Hash Analysis Tool

## Overview
This tool automates the process of analyzing password hashes, identifying the hashing algorithms, and cracking the hashes using either dictionary or brute-force attacks.
It supports common hash algorithms like MD5, SHA1, SHA256, and bcrypt.

## Features
- Identify common hash types (MD5, SHA1, SHA256, bcrypt).
- Crack hashes using dictionary-based attacks (with customizable wordlists).
- Optionally perform brute-force attacks for weak hashes.
- Generate a detailed HTML report on the cracking results.

## Requirements
- Python 3.x
- Required libraries listed in `requirements.txt` (install via `pip`)

## Installation
Clone this repository and install the required dependencies

## Example Output of `cracker.py`

```bash
Enter hash to crack: 5f4dcc3b5aa765d61d8327deb882cf99
Identified hash type: md5
Password cracked: password
Cracking completed in 3.45 seconds.
```


### Generated Report (HTML)

```html
<html>
<head><title>Hash Cracking Report</title></head>
<body>
    <h1>Hash Cracking Report</h1>
    <h2>Hash: 5f4dcc3b5aa765d61d8327deb882cf99</h2>
    <h2>Hash Type: md5</h2>
    <p><b>Cracked Password: </b>password</p>
</body>
</html>
```

### Explanation

1. **Input**: The user is prompted to input a hash value to crack (e.g., `5f4dcc3b5aa765d61d8327deb882cf99`).
2. **Hash Identification**: The script identifies the hash type (`md5` in this case).
3. **Cracking Process**:
   - The script first attempts to crack the hash using a dictionary attack with a wordlist.
   - If the dictionary attack fails, it then attempts brute-force cracking.
   - In this example, the password (`password`) is successfully cracked using the dictionary attack.
4. **Time Taken**: The total cracking time is shown (e.g., `3.45 seconds`).
5. **HTML Report**: A report is generated in HTML format, displaying the hash, hash type, and cracked password.

## Useful resources
[Cracking](https://claudiaslibrary.notion.site/Cracking-12c19f75683280ed9060c3c0fa57f9ca)
