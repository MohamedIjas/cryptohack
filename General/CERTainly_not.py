from Crypto.PublicKey import RSA

# Load the RSA public key from a DER file
key = RSA.importKey(open('2048b-rsa-example-cert.der', 'rb').read())

# Access and print the modulus 'n'
print(key.n)
