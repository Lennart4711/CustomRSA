import random

# All primes from 0 to 1000
FIRST_PRIMES = [
  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 
  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 
  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 
  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
]


def miller_rabin_passed(n: int, iterations: int = 10) -> bool:
    """Probabilistic test if n is prime, error rate: (1/4)**iterations"""
    max_division_by_two = 0
    even_component = n - 1

    while even_component % 2 == 0:
        even_component //= 2
        max_division_by_two += 1
    assert 2**max_division_by_two * even_component == n - 1

    def trial_composite(round_tester: int) -> bool:
        if pow(round_tester, even_component, n) == 1:
            return False

        return all(
            pow(round_tester, 2**i * even_component, n)
            != n - 1
            for i in range(max_division_by_two)
        )

    for _ in range(iterations):
        round_tester = random.randrange(2, n)
        if trial_composite(round_tester):
            return False
    return True


def n_bit_random(n: int) -> int:
    return random.randrange(2 ** (n - 1) + 1, 2**n - 1)


def get_low_level_prime(bits: int) -> int:
    """Generate a prime !candidate! divisible
    by first primes"""
    while True:
        # Obtain a random number
        pc = n_bit_random(bits)
        # Test divisibility by pre-generated primes
        for divisor in FIRST_PRIMES:
            # Number is divisible by another -> not prime
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else:
            # Not divisible by pre-generated primes
            # -> Low Level prime
            return pc


def get_prime(bits: int, rounds: int = 10):
    """Generate a strong pseudoprime with given bit length"""
    while True:
        x = get_low_level_prime(bits)
        if miller_rabin_passed(x, rounds):
            return x