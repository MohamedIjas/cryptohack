from pwn import *  # Import the pwn library for remote connection handling.
from json import loads, dumps  # Import functions to serialize and deserialize JSON data.

# Modulus and exponent for the RSA encryption
n = 0x954e1412ba207b8a246ea515e81425aeb5471cf5062b6497b2c76312ccf150498779ca540464b09fe573df68b0cfdcac124ba799b8546b45b49eaae9fadd630d1b5562a9993c6a3da72d5222e24aa6e1f9c663bfd07f31f0cdef87a54f2fbf7151afc3fd329bd16692dcfa6794c3d94d00fb2e11b49557a491be3e510f0c3e22163487df65e54d68f43a3ecea44e48dc929f2d321c6bfdb2c6c233c704e0618041ace0be91f637f423e6161b36a1fe0f04445ee1f48dc5960659706bbcb97c1667c5f17d0f2395dad348a88f3efb7fa06f99f7963749679eb697cd178fce6f65cfee5b6c9c36096c96f5b5532a6a3b44127afe27f10015dd71a644d455f800d5

# Public exponent
e = 0x10001

# Message to be signed and verified
m = int(bytes.hex(b"admin=True"), 16)  # Convert the message "admin=True" to an integer using hex encoding.

# Connect to the remote server
io = remote("socket.cryptohack.org", 13376)

# Synchronize with the server by receiving the initial line
io.recvline()

# Send the request to sign the message
io.sendline(dumps({"option": "sign", "msg": str(hex((2**e * m) % n))[2:]}).encode())

# Receive the signature from the server, then compute the signature `s` using modular inverse
s = int(loads(io.recvline())["signature"], 16) * pow(2, -1, n) % n

# Send the request to verify the signature
io.sendline(dumps({"option": "verify", "msg": str(hex(m)[2:]), "signature": str(hex(s)[2:])}).encode())

# Print the response from the server indicating whether the verification was successful or not
print(loads(io.recvline())["response"])
