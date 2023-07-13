# secrets module is CSPRNG (Crytophically Secure Pesudo Rando Number Generator)
# Functions 
# randint()
# randrange()
# choice()
# sample()
# shuffle()
# seed()
# uniform()
# triangular() are the same as ramdom module

import secrets

secureGen = secrets.SystemRandom()

# randrange()
print('randrange > ',secureGen.randrange(0,10,2))
print(' ')

# token_bytes(size)
print('token_bytes > ',secrets.token_bytes(4))
print(' ')

# token_hex(size) -> size bytes change to 2xsize hex digits
print('token_hex(4) > ',secrets.token_hex(4))
print(' ')

# token_urlsafe()
link = "https://github.com/Minkhantkyi/Assignment/"
link += secrets.token_urlsafe(4)
print('token_urlsafe(4) > ',link)