import string


def encrypt(message, shift, letter_to_index, index_to_letter):
    cipher = ""

    for letter in message:
        # get the index of each letter from the message, add shift and take modulo of alphabet size
        # ex. for shift = 1, 'a' index will become 0 + 1 = 1 
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        # determine the new letter using index determined previously
        # if index is 2 new letter will be 'b'
        letter = index_to_letter[number]
        # add each letter to cyphered message
        cipher += letter

    return cipher


def decrypt(cipher, shift, letter_to_index, index_to_letter):
    decrypted = ""

    for letter in cipher:
        # same as in encryption, just take back the shift and do modulo of alphabet size
        number = (letter_to_index[letter] - shift) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted


def main():
    message = input('Enter text to be encrypted: ').lower()
    shift = 1
    key = input('Enter your key: ').lower()
    # create new alphabet 
    alphabet = []
    whitespace = ' '
    all_alphabet_letters = string.ascii_lowercase
    # add all unique characters from message
    for character in key:
        if character not in alphabet:
            alphabet += character 
    # add remaining alphabet letters
    for i in all_alphabet_letters:
        if i not in alphabet:
            alphabet.append(i)  
    alphabet.append(whitespace)
    # print new created alphabet
    print('Your new alphabet:')
    print(alphabet)

    # dictionary for mapping between alphabet letter and index, ex. a => 0, b => 1 ... 
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    # an inverse mapping between index and letter 
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))

    cipher = encrypt(message, shift, letter_to_index, index_to_letter)
    decrypted = decrypt(cipher, shift, letter_to_index, index_to_letter)

    print('Your message: ' + message)

    print('Encrypted message: ' + cipher)

    print('Decrypted message: ' + decrypted)


main()
