from sympy import cbrt

c = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

# Calculate the cube root
decoded_number = cbrt(c)

# Convert the cube root result to a hexadecimal string and then to bytes
hex_result = hex(int(decoded_number))[2:]
decoded_message = bytes.fromhex(hex_result).decode()

print(decoded_message)
