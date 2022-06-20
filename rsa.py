from prime import get_prime


def encrypt(num: int, enc_key: tuple) -> int:
    """Encrypt a number using a public key"""
    return pow(num, enc_key[0], enc_key[1])


def decrypt(num: int, dec_key: tuple) -> int:
    """Decrypt a number using a public key"""
    return pow(num, dec_key[0], dec_key[1])


def mod_inverse(a: int, m: int) -> int:
    """The modular inverse is used to calculate the secret key"""
    return pow(a, -1, m)


def gen_keypair(key_length: int = 1024) -> tuple:
    """Generate a keypair with given key length"""
    # 1. Generate 2 random prime numbers, n bit length
    p = get_prime(key_length // 2)
    q = get_prime(key_length // 2)

    # 2. Calculate the product of p and q
    n = p * q

    # 3. Amount of coprimes with n
    phi_n = (p - 1) * (q - 1)

    # 4. e: {1<e<phi_n-1
    #       coprime with n,phi_n
    e = 65537
    # 5. d: (e**-1) mod phi_n
    d = mod_inverse(e, phi_n)

    # 6. Put together the keys
    enc_key = (e, n)
    dec_key = (d, n)

    return enc_key, dec_key
