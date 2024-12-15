# Given keys
key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313

# Calculate key2 by XORing key1 with another constant value
key2 = key1 ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e

# Calculate key3 by XORing key2 with another constant value
key3 = key2 ^ 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1

# Calculate the flag by XORing all the keys and another constant value
flag = key1 ^ key2 ^ key3 ^ 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

# Convert the flag from a hexadecimal representation to bytes, then decode it to a string
print(bytes.fromhex(hex(flag)[2:]).decode())
