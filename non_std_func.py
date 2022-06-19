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
