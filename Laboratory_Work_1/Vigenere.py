
def encrypt(message, key, alphabet, letter_to_index, index_to_letter):
    encrypted = ""
    # split message to the length of key
    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ]
    for each_split in split_message:
        i = 0
        for letter in each_split:
            # each letter from message convert to index, add key and do modulo of alphabet
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            # map the index to the letter of encrypted message
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def decrypt(cipher, key, alphabet, letter_to_index, index_to_letter):
    decrypted = ""
    # split encrypted message to the length of key
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            # inverse operation from encryption, take back index and do modulo of alphabet
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            # map the new index with the corresponding letter
            decrypted += index_to_letter[number]
            i += 1

    return decrypted


def main():
    message = input('Enter text to be encrypted: ').lower()
    key = input('Enter your key:')

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    # dictionary for mapping between alphabet letter and index, ex. a => 0, b => 1 ... 
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    # an inverse mapping between index and letter 
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))

    cipher = encrypt(message, key, alphabet, letter_to_index, index_to_letter)
    decrypted = decrypt(cipher, key, alphabet, letter_to_index, index_to_letter)

    print("Your message: " + message)

    print("Encrypted message: " + cipher)

    print("Decrypted message: " + decrypted)


main()