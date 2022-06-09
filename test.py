import time
from prime import getPrime
import numpy as np



def iterPrime(iters=20, n=128):
    t = []
    for _ in range(iters):
        s = time.time()
        getPrime(n)
        t.append(time.time()-s)
    return t

bits = [64, 128, 256, 512, 1024]

stimes = []
for bit in bits:
    print(bit)
    stimes.append(iterPrime(100, bit))

    
for entry in stimes:
    print(np.mean(entry))
