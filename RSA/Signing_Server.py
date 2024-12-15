from pwn import *  # Importing the pwn library for easier remote connection handling and exploitation tasks.
from json import dumps, loads  # Importing functions to serialize and deserialize JSON data.

# Establish a remote connection to the server.
io = remote("socket.cryptohack.org", 13374)

# Receive the first line from the server.
io.recvline()

# Send a request to get the secret using JSON serialization.
io.sendline(dumps({"option": "get_secret"}).encode())

# Receive the secret from the server, parse it from the JSON response, and use it in the next request.
secret = loads(io.recvline())["secret"]

# Send a request to sign the secret using JSON serialization.
io.sendline(dumps({"option": "sign", "msg": secret}).encode())

# Receive the signature from the server, parse it from the JSON response, and convert it from hexadecimal to ASCII.
signature_hex = loads(io.recvline())["signature"][2:]  # Strip off the '0x' prefix
signature = bytes.fromhex(signature_hex).decode()  # Convert from hex to ASCII

# Print the decoded signature
print(signature)
