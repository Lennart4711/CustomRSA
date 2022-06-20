# Naive method
def mod_inverse_naive(a, m):
    return next((x for x in range(1, m) if (((a % m) * (x % m)) % m == 1)), -1)


# Euclid algorithm
def mod_inverse_euclid(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0

    while a > 1:
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
    if x < 0:
        x += m0

    return x


# Custom Modular Exponantiation, euqivalent to pow(b,e,m)
def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    c = 1
    base = base % modulus
    for _ in range(exponent):
        c = (c * base) % modulus
    return c


def is_prime_deterministic(n: int) -> bool:
    """Determinstic test if n is prime"""
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    for f in range(5, r + 1, 6):
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
    return True