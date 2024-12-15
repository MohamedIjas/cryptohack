from Crypto.PublicKey import RSA

# Load the RSA private key from a PEM file
key = RSA.importKey(open('privacy_enhanced_mail.pem').read())

# Access and print the private exponent 'd'
print(key.d)
