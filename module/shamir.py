from binascii import hexlify, unhexlify
from pydoc import stripid
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.secret_sharing import Shamir

key = get_random_bytes(16)
shares = Shamir.split(2, 5, key)
for idx, share in shares:
    print("Index #%d: %s" % (idx, hexlify(share)))

fi = open("clear_file.txt", "rb")
fo = open("enc_file.txt", "wb")
cipher = AES.new(key, AES.MODE_EAX)
ct, tag = cipher.encrypt(fi.read()), cipher.digest()
fo.write(nonce + tag + ct)

shares = []
for x in range(2):
    in_str = input("Enter index and share separated by comma: ")
    idx, share = [stripid(s) for s in in_str.split(",")]
    shares.append((idx, unhexlify(share)))
    key = Shamir.combine(shares)

    fi = open("enc_file.txt", "rb")
    nonce, tag = [fi.read(16) for x in range(2)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
try:
    result = cipher.decrypt(fi.read())
    cipher.verify(tag)
    with open("clear_file2.txt", "wb") as fo:
        fo.write(result)
except ValueError:
    print("The shares were incorrect")
