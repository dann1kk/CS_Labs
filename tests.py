from email import message
from Ciphers import stream
from Ciphers import vigenere
from Ciphers import caesar_substitution
from Ciphers import caesar_permutation
from Ciphers import playfair
from Ciphers import block
from Ciphers import rsa 

def main():
    
    message1 = "GOOD MORNING"
    message2 = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
    message3 = "hEllO wOrLd"
    message1_stream = "YOU FU###### DONKEY"
    message2_stream = "3.145432342"
    message3_stream = "daniel.pogorevici@isa.utm.md"
    message1_block = "XD123%$#"
    message2_block = "ThisT3st"
    message3_block = "Wi11Work"
    key = "secretik"
   
 
    print("\nCAESAR CIPHER")
    cipher1 = caesar_substitution.encrypt(message1.lower(), caesar_substitution.shift, caesar_substitution.letter_to_index, caesar_substitution.index_to_letter)
    decrypted1 = caesar_substitution.decrypt(cipher1, caesar_substitution.shift, caesar_substitution.letter_to_index, caesar_substitution.index_to_letter)
    cipher2 = caesar_substitution.encrypt(message2.lower(), caesar_substitution.shift, caesar_substitution.letter_to_index, caesar_substitution.index_to_letter)
    decrypted2 = caesar_substitution.decrypt(cipher2, caesar_substitution.shift, caesar_substitution.letter_to_index, caesar_substitution.index_to_letter)
    cipher3 = caesar_substitution.encrypt(message3.lower(), caesar_substitution.shift, caesar_substitution.letter_to_index, caesar_substitution.index_to_letter)
    decrypted3 = caesar_substitution.decrypt(cipher3, caesar_substitution.shift, caesar_substitution.letter_to_index, caesar_substitution.index_to_letter)
    print('Your message: ' + message1)
    print('Encrypted message: ' + cipher1)
    print('Decrypted message: ' + decrypted1)
    print('\nYour message: ' + message2)
    print('Encrypted message: ' + cipher2)
    print('Decrypted message: ' + decrypted2)
    print('\nYour message: ' + message3)
    print('Encrypted message: ' + cipher3)
    print('Decrypted message: ' + decrypted3)


    print("\nCAESAR CIPHER WITH PERMUTATION")
    cipher1 = caesar_permutation.encrypt(message1.lower(), caesar_permutation.shift, caesar_permutation.letter_to_index, caesar_permutation.index_to_letter)
    decrypted1 = caesar_permutation.decrypt(cipher1, caesar_permutation.shift, caesar_permutation.letter_to_index, caesar_permutation.index_to_letter)
    cipher2 = caesar_permutation.encrypt(message2.lower(), caesar_permutation.shift, caesar_permutation.letter_to_index, caesar_permutation.index_to_letter)
    decrypted2 = caesar_permutation.decrypt(cipher2, caesar_permutation.shift, caesar_permutation.letter_to_index, caesar_permutation.index_to_letter)
    cipher3 = caesar_permutation.encrypt(message3.lower(), caesar_permutation.shift, caesar_permutation.letter_to_index, caesar_permutation.index_to_letter)
    decrypted3 = caesar_permutation.decrypt(cipher3, caesar_permutation.shift, caesar_permutation.letter_to_index, caesar_permutation.index_to_letter)
    print('\nYour message: ' + message1)
    print('Encrypted message: ' + cipher1)
    print('Decrypted message: ' + decrypted1)
    print('\nYour message: ' + message2)
    print('Encrypted message: ' + cipher2)
    print('Decrypted message: ' + decrypted2)
    print('\nYour message: ' + message3)
    print('Encrypted message: ' + cipher3)
    print('Decrypted message: ' + decrypted3)

    print("\nVIGENERE CIPHER")
    cipher1 = vigenere.encrypt(message1.lower(), key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
    decrypted1 = vigenere.decrypt(cipher1, key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
    cipher2 = vigenere.encrypt(message2.lower(), key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
    decrypted2 = vigenere.decrypt(cipher2, key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
    cipher3 = vigenere.encrypt(message3.lower(), key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
    decrypted3 = vigenere.decrypt(cipher3, key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
    print("\nYour message: " + message1)
    print("Encrypted message: " + cipher1)
    print("Decrypted message: " + decrypted1)
    print("\nYour message: " + message2)
    print("Encrypted message: " + cipher2)
    print("Decrypted message: " + decrypted2)
    print("\nYour message: " + message3)
    print("Encrypted message: " + cipher3)
    print("Decrypted message: " + decrypted3)

    print("\nPLAYFAIR CIPHER")
    cipher1 = playfair.encrypt(message1, key)
    decrypted1 = playfair.decrypt(cipher1, key)
    cipher2 = playfair.encrypt(message2, key)
    decrypted2 = playfair.decrypt(cipher2, key)
    cipher3 = playfair.encrypt(message3, key)
    decrypted3 = playfair.decrypt(cipher3, key)
    print("\nYour message: " + message1)
    print("Encrypted message: " + cipher1)
    print("Decrypted message: " + decrypted1)
    print("\nYour message: " + message2)
    print("Encrypted message: " + cipher2)
    print("Decrypted message: " + decrypted2)
    print("\nYour message: " + message3)
    print("Encrypted message: " + cipher3)
    print("Decrypted message: " + decrypted3)

    print("\nSTREAM CIPHER")
    newKey = stream.randomKey()
    print("Your new key is: ", newKey)
    for i in range(2):
        encryption1 = stream.encrypt(message1_stream, newKey)
        res1 = stream.encrypt(encryption1, newKey)
        encryption2 = stream.encrypt(message2_stream, newKey)
        res2 = stream.encrypt(encryption2, newKey)
        encryption3 = stream.encrypt(message3_stream, newKey)
        res3 = stream.encrypt(encryption3, newKey)
    print("\nEncrypted message is: " + res1)
    print("Encrypted message is: " + res2)
    print("Encrypted message is: " + res3)
    for i in range(2):
        decryption1 = stream.decrypt(res1, newKey)
        res4 = stream.decrypt(decryption1, newKey)
        decryption2 = stream.decrypt(res2, newKey)
        res5 = stream.decrypt(decryption2, newKey)
        decryption3 = stream.decrypt(res3, newKey)
        res6 = stream.decrypt(decryption3, newKey)
    print("\nDecrypted message is:" + res4)
    print("Decrypted message is:" + res5)
    print("Decrypted message is:" + res6)

    print("\nBLOCK CIPHER")
    b_ciph = block.blowfish(key)
    encrypted1 = b_ciph.encrypt (message1_block)
    decrypted_bytes1 = b_ciph.decrypt (encrypted1)
    decrypted1 = decrypted_bytes1.decode()
    encrypted2 = b_ciph.encrypt (message2_block)
    decrypted_bytes2 = b_ciph.decrypt (encrypted2)
    decrypted2 = decrypted_bytes2.decode()
    encrypted3 = b_ciph.encrypt (message3_block)
    decrypted_bytes3 = b_ciph.decrypt (encrypted3)
    decrypted3 = decrypted_bytes3.decode()
    print("\nYour message: " + message1_block)
    print("Encrypted: " + encrypted1)
    print("Decrypted: " + decrypted1)
    print("\nYour message: " + message2_block)
    print("Encrypted: " + encrypted2)
    print("Decrypted: " + decrypted2)
    print("\nYour message: " + message3_block)
    print("Encrypted: " + encrypted3)
    print("Decrypted: " + decrypted3)

    print("\nRSA CIPHER")
    public, private = rsa.generate_key_pair(rsa.p, rsa.q)
    print("Public key: ", public)
    print("Private key: ", private)
    encrypted1 = rsa.encrypt(public, message1)
    decrypted1 = rsa.decrypt(private, encrypted1)
    encrypted2 = rsa.encrypt(public, message2)
    decrypted2 = rsa.decrypt(private, encrypted2)
    encrypted3 = rsa.encrypt(public, message3)
    decrypted3 = rsa.decrypt(private, encrypted3)
    print("\nYour message: " + message1)
    print("Encrypted: ", ''.join(map(lambda x: str(x) + " ", encrypted2)))
    print("Decrypted: ", decrypted1)
    print("\nYour message: " + message2)
    print("Encrypted: ", ''.join(map(lambda x: str(x) + " ", encrypted2)))
    print("Decrypted: ", decrypted2)
    print("\nYour message: " + message3)
    print("Encrypted: ", ''.join(map(lambda x: str(x) + " ", encrypted3)))
    print("Decrypted: ", decrypted3)


main()
