from pwn import xor

# Encrypted message in hexadecimal format
enc = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# Key used for XOR decryption
key = b'myXORkey'

# Decrypt the message using XOR with the given key
# `xor(enc, key)` will apply XOR to each byte in `enc` with the corresponding byte in `key`
# `decode()` will convert the resulting bytes back to a string
print(xor(enc, key).decode())
