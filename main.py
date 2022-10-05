from Ciphers import stream
from Ciphers import vigenere
from Ciphers import caesar_substitution
from Ciphers import caesar_permutation
from Ciphers import playfair
from Ciphers import block

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


main()