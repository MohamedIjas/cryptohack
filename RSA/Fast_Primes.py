from Crypto.Cipher import PKCS1_OAEP

# Public and private key parameters
e = 65537  # Public exponent
c = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28  # Ciphertext (hexadecimal)
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469  # Prime factor of n
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161  # Prime factor of n

# Compute the RSA modulus n
n = p * q

# Compute the private key exponent d using the modular inverse
d = pow(e, -1, (p - 1) * (q - 1))  # d = e^(-1) mod φ(n), where φ(n) = (p-1)*(q-1)

# Construct the RSA key object
key = RSA.construct((n, e, d))

# Initialize the RSA cipher in OAEP mode
cipher = PKCS1_OAEP.new(key)

# Decrypt the ciphertext
decrypted_message = cipher.decrypt(bytes.fromhex(hex(c)[2:])).decode()

# Output the decrypted plaintext
print(decrypted_message)
