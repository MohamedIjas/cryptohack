from pwn import remote
from json import loads, dumps

# Connect to the remote service
io = remote('socket.cryptohack.org', 13403)

# Receive the message with the prime value
io.readuntil(b'Prime generated: "')

# Read and convert the prime value from hexadecimal to integer
q = int(io.readline()[:-2], 16)

# Send the response using the g and n values derived from the prime q
# g = q + 1 and n = q^2
io.sendline(dumps({"g":hex(q+1), "n":hex(q**2)}).encode())

# Receive the message with the generated public key
io.readuntil(b'Generated my public key: "')

# Read and convert the public key from hexadecimal to integer
pub = int(io.readline()[:-2], 16)

# Send the response with the private key derived from the public key
# x = (pub - 1) // q
io.sendline(dumps({"x":hex((pub-1)//q)}).encode())

# Receive the message indicating what is the private key
io.readuntil(b'What is my private key: ')

# Print the flag extracted from the server response
print(loads(io.readline().decode())['flag'])
