# Given encrypted message in hexadecimal
enc = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# Calculate the key by XORing the first byte of the encrypted message with the ASCII value of 'c'
key = enc[0] ^ ord('c')

# Decrypt the message by XORing each byte of the encrypted message with the key
# The decrypted characters are then joined into a string
print(''.join(chr(c ^ key) for c in enc))
