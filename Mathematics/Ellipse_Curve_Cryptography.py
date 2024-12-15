from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha1

# Given shared secret
shared_secret = 83201481069630956436480435779471169630605662777874697301601848920266492

# Generate AES key using SHA-1 hash
# Convert the shared secret to a string and then encode it to ASCII bytes
# Generate the SHA-1 digest and take the first 16 bytes for the AES key
key = sha1(str(shared_secret).encode('ascii')).digest()[:16]

# Given IV (Initialization Vector) in hex
iv = bytes.fromhex('64bc75c8b38017e1397c46f85d4e332b')

# Given encrypted flag in hex
encrypted_flag = bytes.fromhex('13e4d200708b786d8f7c3bd2dc5de0201f0d7879192e6603d7c5d6b963e1df2943e3ff75f7fda9c30a92171bbbc5acbf')

# Create AES cipher object using the key, CBC mode, and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the encrypted flag and remove padding
# unpad(cipher.decrypt(encrypted_flag), 16) removes the PKCS7 padding
print(unpad(cipher.decrypt(encrypted_flag), 16).decode())
