from binascii import hexlify
from Crypto.Protocol.SecretSharing import Shamir
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'my big secret it is my secret'   # 9 bytes
key = get_random_bytes(32)
iv = get_random_bytes(16)


shares = Shamir.split(2, 5, iv)
for idx, share in shares:
    print("Index %d: %s" % (idx, hexlify(share)))

with open("encrypted.bin", "rb") as fi, open("encrypted.bint", "wb") as fo:
    cipher1 = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher1.encrypt(pad(data, 16))
    fo.write(ct)


shares = []
in_str = input("Enter index and share separated by comma: ")
for x in range(2):
    idx, share = [s.strip() for s in in_str.split(",")]
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher2.decrypt(ct), 16)
assert(data == pt)

print("secret reconstruct is"+pt)
