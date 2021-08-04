# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 22:31:04 2019

@author: ms
"""

#!/usr/bin/env python3

import argparse
from Crypto.Cipher import AES
import getpass
import hashlib
import sys

#filepath = 'C:/Users/ms/Disk Google/journal.txt'

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="journal file to decrypt")
args = parser.parse_args()

pwd = getpass.getpass()
key = hashlib.sha256(pwd.encode('utf-8')).digest()

with open(filepath, 'rb') as f:
    ciphertext = f.read()

crypto = AES.new(key, AES.MODE_CBC, ciphertext[:16])
plain = crypto.decrypt(ciphertext[16:])
plain = plain.strip(plain[-1:])
plain = plain.decode("utf-8")
print(plain)