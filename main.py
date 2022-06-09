import random
from prime import getPrime
import cProfile
import time

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
    return pow(num, enc_key[0], enc_key[1])
    #return modular_pow(num, enc_key[0], enc_key[1])

def decrypt(num, dec_key):
    return pow(num, dec_key[0], dec_key[1])
    #return modular_pow(num, dec_key[0], dec_key[1])

# Naive method
def mod_inverse_naive(a, m):
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

def mod_inverse(a,m):
    return pow(a,-1,m)

# -----Generate keys---------
key_length = 1024
# 1. Generate 2 random prime numbers, n bit length
p = getPrime(key_length/2)
q = getPrime(key_length/2)

# 2. Calculate the product of p and q
n = p*q

# 3. Amount of coprimes with n
phi_n = (p-1)*(q-1)

# 4. e: {1<e<phi_n
#       coprime with n,phi_n
e = 65537
# 5. d: de(mod phi_n) = 1
d = mod_inverse_euclid(e, phi_n)

# 6. Put together the keys
enc_key = (e,n)
dec_key = (d,n)


#------ Example --------
# 1. A clear text represented as a number
clear_text = 110100001100101011011000110110001101111001000000111011101101111011100100110110001100100

# 2. Encrypt using the public key
chiffre = encrypt(clear_text, enc_key)

# 3. Decrypt using the private key
original = decrypt(chiffre, dec_key)




print(f"p: {p}, q: {q}")
print("n:",n)   
print("phi_n:",phi_n)
print("enc_key =",enc_key)
print("dec_key =", dec_key)
print(clear_text)
print(chiffre)
print(original)