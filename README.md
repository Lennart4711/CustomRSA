# CustomRSA
Custom implementation of the RSA-Algorithm. Used for fundamental understanding of the RSA algorithm
and generation of prime numbers. 

## Explanation/ Usage of the functions in the files
### prime.py
Functions to deal with generating prime numbers

```python
# Generate a prime number with length n bits
n_bit_random(n)

# Generate a number with length n bits that is coprime with every prime up to 1000
get_low_level_prime(n)

# Miller-Rabin-Test on n, optional argument: number of rounds
miller_rabin_passed(n, k)

# Get_low_level_prime and miller_rabin_passed combined to
# get a strong pseudoprime of length n bits
# Optional argument: number of rounds
get_prime(n, k)
```

### rsa.py
Implementation of the RSA algorithm.
```python
# Generate a pair of public/private keys with length n bits
gen_keypair(n)

# Modular inverse, used to caluclate the private key
mod_inverse(a, m)
# Same as
pow(a, -1, m)

# Encrypt a number using a public key
encrypt(num, public_key)

# Decrypt a number using a private key
decrypt(cipher, private_key)
```
### messanger.py 
Express string as number, then encrypt/ decrypt using a key pair
```python
# Print only first and last n digits of a string or int
pprint(str)
# Lorem Ipsum dolor sit amet -> Lorem... amet (26)

# Encrypt a string by converting it to a custom integer representation
encrypt(msg, public_key)

# Decrypt an integer and return it as a string
decrypt(msg, public_key)
```
## TODO
- Figure out, why maximum text length for 2048 bit key is 205
- Implement padding to prevent "Textbook-RSA"-attacks
- Use different, more known encoding like ASCII