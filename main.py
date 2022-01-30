import random
from prime import is_prime

# Custom Modular Exponantiation, euqivalent to pow(b,e,m)
def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    c = 1
    base = base % modulus
    for _ in range(exponent):
        c = (c*base) % modulus
    return c

def encrypt(num, enc_key):
    return modular_pow(num, enc_key[0], enc_key[1])

def decrypt(num, dec_key):
    return modular_pow(num, dec_key[0], dec_key[1])

# Naiv method
def mod_inverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

# Euclid algorithm 
def mod_inverse_euclid(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if (x < 0):
        x += m0

    return x

# Generate p,q as two random primes
primes = [i for i in range(1000,9999) if is_prime(i)]
p,q= random.sample(primes, 2)
#p,q = 6719, 4729
print(f"p: {p}, q: {q}")
n = p*q
print("n:",n)
phi_n = (p-1)*(q-1)
print("phi_n:",phi_n)

# e = None
# for i in range(max(p,q)+1, max(p, q)*100):
#     if is_prime(i):
#         e = i
#         break
# if e is None:
#     raise "No encryption key found"
e = 65537

d = mod_inverse_euclid(e, phi_n)

enc_key = (e,n)
dec_key = (d,n)
print("enc_key:",enc_key)
print("dec_key:", dec_key)


clear_text = 1234568
print(clear_text)

chiffrat = encrypt(clear_text, enc_key)
print(chiffrat)

out = decrypt(chiffrat, dec_key)
print(out)

