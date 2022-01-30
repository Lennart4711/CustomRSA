import random
from prime import is_prime


def text_to_numbers(char):
    return str(alphabet.find(char))

def encrypt(num, enc_key):
    return pow(num, enc_key[0], enc_key[1])


def decrypt(num, dec_key):
    return pow(num, dec_key[0], dec_key[1])

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


primes = [i for i in range(10000,99999) if is_prime(i)]
p,q= random.sample(primes, 2)
#p,q = 809, 233
print(f"p: {p}, q: {q}")
n = p*q
print("n:",n)
phi_n = (p-1)*(q-1)
print("phi_n:",phi_n)

e = None
for i in range(max(p,q)+1, max(p, q)*100):
    if is_prime(i):
        e = i
        break
if e is None:
    raise "No encryption key found"

d = modInverse(e, phi_n)

enc_key = (e,n)
dec_key = (d,n)
print("enc_key:",enc_key)
print("dec_key:", dec_key)


clear_text = 18712345
print(clear_text)

chiffrat = encrypt(clear_text, enc_key)
print(chiffrat)

out = decrypt(chiffrat, dec_key)
print(out)
