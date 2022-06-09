from Crypto.Util import number
import time

from prime import getPrime

start = time.time()
for i in range(100):
    getPrime(1024)
    print(i)
print(time.time() - start)

start = time.time()
for i in range(100):
    number.getPrime(1024)
    print(i)
print(time.time() - start)
    
