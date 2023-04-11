import encode as en
import random
from Crypto.Random import get_random_bytes
from Crypto.Util import number
import math



def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def generate_keys(key_size):
    # Choose two random prime numbers
    p = number.getPrime(key_size)

    q = number.getPrime(key_size)
    while p == q:
        q = number.getPrime(key_size)

    # Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose a random integer e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Calculate d such that d*e ≡ 1 (mod phi_n)
    d = pow(e, -1, phi_n)

    return (n, e), (n, d)


def encrypt(message, public_key):
    n, e = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    n, d = private_key
    return pow(ciphertext, d, n)




    