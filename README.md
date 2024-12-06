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
Clone this repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/password_cracking_tool.git
cd password_cracking_tool
pip install -r requirements.txt
```
