from Crypto.PublicKey import RSA

# Load the RSA public key from the file
key = RSA.importKey(open('bruce_rsa.pub').read())

# Access and print the modulus 'n'
print(key.n)
