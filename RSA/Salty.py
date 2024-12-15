c = 44981230718212183604274785925793145442655465025264554046028251311164494127485
# Convert the number to hexadecimal and remove the '0x' prefix
hex_c = hex(c)[2:]
# Convert the hexadecimal string to bytes
byte_c = bytes.fromhex(hex_c)
# Decode the bytes to a string
decoded_message = byte_c.decode()

print(decoded_message)
