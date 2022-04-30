from binascii import hexlify, unhexlify
import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.SecretSharing import Shamir
from flask import Flask
app = Flask(__name__)

data = b'creation de mot de passe secret big secret'
# Encryption
key = get_random_bytes(16)

partage = Shamir.split(2, 5, key)
for i, p in partage:
    print("Index %d: %s" % (i, hexlify(p)))
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()

    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    # nonce, tag = [file_in.read(16) for x in range(2)]
# let's assume that the key is somehow available again
partage = []
in_str = input("Enter index and share separated by comma: ")
for x in range(2):
    
    i, p = [in_str.strip(s) for s in in_str.split(",")]

    key = Shamir.combine(partage)
with open("encrypted.bin", "rb") as file_in:
    nonce, tag = [file_in.read(16) for x in range(2)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
try:
    result = cipher.decrypt(file_in.read())
    cipher.verify(tag)
    with open("encrypted.bin", "wb") as file_out:
        file_out.write(result)
except ValueError:
    print("The shares were incorrect")
