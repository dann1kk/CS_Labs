from Ciphers import stream
from Ciphers import vigenere
from Ciphers import caesar_substitution
from Ciphers import caesar_permutation
from Ciphers import playfair
from Ciphers import block
from Ciphers import rsa
from Ciphers import sha256
import struct, codecs, hashlib
db = []

def main():
    
    message = input("Enter text to be encrypted: ")
    key = input('Enter your key:')
    message_block = input('Enter 8 bytes message: ')
    message_lower = message.lower()
 
    print("CAESAR CIPHER")
    cipher = caesar_substitution.encrypt(message_lower, caesar_substitution.shift, caesar_substitution.letter_to_index, caesar_substitution.index_to_letter)
    decrypted = caesar_substitution.decrypt(cipher, caesar_substitution.shift, caesar_substitution.letter_to_index, caesar_substitution.index_to_letter)
    print('Your message: ' + message)
    print('Encrypted message: ' + cipher)
    print('Decrypted message: ' + decrypted)

    print("CAESAR CIPHER WITH PERMUTATION")
    cipher = caesar_permutation.encrypt(message_lower, caesar_permutation.shift, caesar_permutation.letter_to_index, caesar_permutation.index_to_letter)
    decrypted = caesar_permutation.decrypt(cipher, caesar_permutation.shift, caesar_permutation.letter_to_index, caesar_permutation.index_to_letter)
    print('Your message: ' + message_lower)
    print('Encrypted message: ' + cipher)
    print('Decrypted message: ' + decrypted)

    print("VIGENERE CIPHER")
    cipher = vigenere.encrypt(message_lower, key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
    decrypted = vigenere.decrypt(cipher, key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
    print("Your message: " + message)
    print("Encrypted message: " + cipher)
    print("Decrypted message: " + decrypted)

    print("PLAYFAIR CIPHER")
    cipher = playfair.encrypt(message, key)
    decrypted = playfair.decrypt(cipher, key)
    print("Your message: " + message)
    print("Encrypted message: " + cipher)
    print("Decrypted message: " + decrypted)

    print("STREAM CIPHER")
    newKey = stream.randomKey()
    print("Your new key is: ", newKey)
    for i in range(2):
        encryption = stream.encrypt(message, newKey)
        res = stream.encrypt(encryption, newKey)
    print("Encrypted message is: " + res)
    for i in range(2):
        decryption = stream.decrypt(res, newKey)
        res2 = stream.decrypt(decryption, newKey)
    print("Decrypted message is:" + res2)

    print("BLOCK CIPHER")
    b_ciph = block.blowfish(key)
    encrypted = b_ciph.encrypt (message_block)
    decrypted_bytes = b_ciph.decrypt (encrypted)
    decrypted = decrypted_bytes.decode()
    print("Your message: " + message_block)
    print("\tEncrypted: " + encrypted)
    print("\tDecrypted: " + decrypted)

    print("RSA CIPHER")
    public, private = rsa.generate_key_pair(rsa.p, rsa.q)
    print("Public key: ", public)
    print("Private key: ", private)
    encrypted = rsa.encrypt(public, message)
    decrypted = rsa.decrypt(private, encrypted)
    print("Your message: " + message)
    print("Encrypted: ", ''.join(map(lambda x: str(x) + " ", encrypted)))
    print("Decrypted: ", decrypted)

    print("SHA256 HASHING:")
    byte_message = bytes(message, 'UTF-8')
    print("Preprocess the message as a string to bytes: ", byte_message)
    digest = codecs.encode(sha256.sha256_sum(byte_message), 'hex').decode()
    db.append(digest)
    print("Message digest: ", digest)
    encrypted = rsa.encrypt(public, digest)
    db.append(encrypted)
    print("Encrypted message using RSA cipher:" , encrypted)
    encrypted_db = db[1]
    decrypted = rsa.decrypt(private, encrypted_db)
    digest_db = db[0]
    print("Decrypted message:", decrypted)
    if (decrypted == digest_db):
        print("Digital signature check successfully performed!")
    else:
        print("Error!")


main()