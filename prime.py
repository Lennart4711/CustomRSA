import random
import time

# All primes from 0 to 10000
first_primes_list = [
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 
449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 
587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 
853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
]

def is_prime_deterministic(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  for f in range(5, r + 1, 6):
    if n % f == 0: return False
    if n % (f+2) == 0: return False
  return True  


def isMillerRabinPassed(miller_rabin_candidate, iterations=20):   
    maxDivisionsByTwo = 0
    evenComponent = miller_rabin_candidate-1
   
    while evenComponent % 2 == 0:
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * evenComponent == miller_rabin_candidate-1)
   
    def trialComposite(round_tester):
      if pow(round_tester, evenComponent, 
             miller_rabin_candidate) == 1:
          return False

      return all(
          pow(round_tester, 2**i *
              evenComponent, miller_rabin_candidate) != miller_rabin_candidate - 1
          for i in range(maxDivisionsByTwo))
   
    for _ in range(iterations):
        round_tester = random.randrange(2, miller_rabin_candidate)
        if trialComposite(round_tester):
            return False
    return True

def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)
 
def getLowLevelPrime(n):
    '''Generate a prime candidate divisible
    by first primes'''
    while True:
        # Obtain a random number
        pc = nBitRandom(n)
         # Test divisibility by pre-generated
         # primes
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else: return pc

def getPrime(n):
  start = time.time()
  while True:
    #x = nBitRandom(n)
    x = getLowLevelPrime(n)
    if isMillerRabinPassed(x):
      return x