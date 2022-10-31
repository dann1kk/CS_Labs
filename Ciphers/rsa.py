import random
from Ciphers.cipher import Cipher
from math import gcd
from math import sqrt

from sympy import isprime

p = int(random.randrange(1, 10000))
q = int(random.randrange(1, 10000))
# generate numbers until prime
while not isprime(p):
    p = int(random.randrange(1, 10000))
while not isprime(q):
    q = int(random.randrange(1, 10000))

# generate key pair with requirements
def generate_key_pair(p, q):
    if not (isprime(p) and isprime(q)):
        raise ValueError('Must be prime numbers!')
    elif p == q:
        raise ValueError('Must be not the same numbers!')
    n = p * q

    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)
    # determining gcd
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))
# calculate multiplicative inverse
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi
# encryption of message using public key 
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

# decryption with private key
def decrypt(pk, ciphertext):
    key, n = pk
    dba = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in dba]
    return ''.join(plain)

