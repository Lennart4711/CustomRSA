from rsa import encrypt, decrypt, gen_keypair

ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ' ', '.', '!', '?', ',', ':'
]


def chr_to_num(c: str) -> int:
    """Encodes a char using custom encoding"""
    return 128 + ALPHABET.index(c)


def num_to_chr(num: int) -> str:
    """Decodes an integer to a chr using custom encoding"""
    return ALPHABET[num - 128]


def encrypt_msg(msg: str, enc_key: tuple) -> int:
    """This function encodes and encrypts the message provided."""
    # List of every char in msg as number
    chars = [str(chr_to_num(c)) for c in msg]
    # Join to one long int
    x = int("".join(chars))
    # Decrypt the msg
    return encrypt(x, enc_key)


def decrypt_msg(msg: int, dec_key: tuple) -> str:
    """This function decrypts and decodes a string back into plain text."""
    # Decrypt the decoded msg
    decoded = str(decrypt(msg, dec_key))
    # Split at every third decimal places for 8 bit
    char_nums = [decoded[i : i + 3] for i in range(0, len(decoded), 3)]
    # Get original char from number representation
    chars = [num_to_chr(int(x)) for x in char_nums]
    # List of chars to string
    return "".join(chars)


def pprint(msg, length: int=5) -> str:
    return f"{str(msg)[:length]}...{str(msg)[-length:]} ({len(str(msg))})"

if __name__ == "__main__":
    print("Generating keypair...")
    enc_key, dec_key = gen_keypair(2048)

    cleartext = ":"*205
    print(f"Cleartext: {pprint(cleartext)}")

    ciphertext = encrypt_msg(cleartext.lower(), enc_key)
    print(f"Ciphertext: {pprint(ciphertext)} {ciphertext.bit_length()}")

    f = decrypt_msg(ciphertext, dec_key)
    print(f"Encrypted: {pprint(f)}", )