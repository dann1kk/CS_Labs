# RSA Cipher

## Theory
&ensp;&ensp;&ensp;  RSA algorithm is an asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. As the name describes that the Public Key is given to everyone and the Private key is kept private.

## Implementation
&ensp;&ensp;&ensp; This is an example of RSA algorithm which follows all the required steps:
1. generating two numbers and checking if they are prime (for that I use isprime from sympy)
2. determining the greatest common divisor (imported gcd from math)
3. determining the multiplicative inverse
4. perform encryption and decryption

### Initial Steps:
&ensp;&ensp;&ensp; For the start is generation of key pairs from generated prime numbers.
```
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
```
&ensp;&ensp;&ensp; Afterwards we determine the multiplicative inverse, using previously determined phi and a random number in the interval from 1 to phi
```
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
```

### Encryption
&ensp;&ensp;&ensp; At the encryption part we determine the unicode of each character in plaintext, afterwards compute ciphertext using public key. 
```
# encryption of message using public key 
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher
```

### Decryption 
&ensp;&ensp;&ensp; In the decryption I reverse the padding scheme, using the private key I determine the unicode of each character in the string and find the matching char for it.
```
# decryption with private key
def decrypt(pk, ciphertext):
    key, n = pk
    dba = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in dba]
    return ''.join(plain)
```
## Screenshots
![](https://github.com/dann1kk/CS_Labs/blob/main/Resources/rsa.png)