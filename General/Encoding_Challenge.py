from pwn import remote
from json import loads, dumps
from base64 import b64decode
from codecs import encode

# Connect to the remote service
io = remote('socket.cryptohack.org', 13377)

# Infinite loop to keep receiving and processing data
while True:
    # Receive a line from the server and decode it as JSON
    enc = loads(io.recvline().decode())
    
    # Print the received encrypted message for debugging
    print(enc)
    
    # Check if the 'flag' key is in the received JSON
    if 'flag' in enc:
        # If 'flag' is found, break out of the loop
        break
    
    # Process the received encoded message based on its type
    io.sendline(dumps({
        "decoded": {
            'base64': lambda e: b64decode(e).decode(),  # Decode base64 to UTF-8
            'hex'   : lambda e: bytes.fromhex(e).decode(),  # Decode hex to UTF-8
            'rot13' : lambda e: encode(e, 'rot_13'),  # Apply ROT13 cipher
            'bigint': lambda e: bytes.fromhex(e[2:]).decode(),  # Convert bigint from hex to UTF-8
            'utf-8' : lambda e: ''.join([chr(c) for c in e])  # Convert list of integers to UTF-8 string
        }[enc['type']](enc['encoded'])
    }).encode())
