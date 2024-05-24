import sys
from hashlib import sha256
from Crypto.Util.number import getPrime, bytes_to_long

if len(sys.argv) < 4:
    print("Usage: python script_name.py <firmware_file> <signature_file>")
    sys.exit(1)

firmwarefile = sys.argv[1]
with open(firmwarefile, "rb") as file:
    firmwarefile = file.read()

hasher = sha256()
hasher.update(firmwarefile)
hash_firmware = bytes_to_long(hasher.digest())

sign_file = sys.argv[2] 
p = getPrime(1024)
q = getPrime(1024)
n = p * q
phi = (p - 1) * (q - 1)
e = (2 ** 16) + 1
d = pow(e, -1, phi)

signature = pow(hash_firmware, d, n)
with open(sign_file, "w") as output_sign: 
    output_sign.write(str(signature))

with open("public_key.txt", "w") as public:
    public.write(str(e) + "\n")
    public.write(str(n))
