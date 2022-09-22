import string
import itertools

def chunker(seq, size):
    it = iter(seq)
    while True:
       chunk = tuple(itertools.islice(it, size))
       if not chunk:
           return
       yield chunk


def prepare_input(initial_message):
    # preparing the input message by converting it to uppercase
    # and separating repeated letters with X's
    initial_message = ''.join([c.upper() for c in initial_message if c in string.ascii_letters])
    final_message = ""
    
    if len(initial_message) < 2:
        return initial_message

    for i in range(len(initial_message)-1):
        final_message += initial_message[i]
        
        if initial_message[i] == initial_message[i+1]:
            final_message += 'X'
    
    final_message += initial_message[-1]

    if len(final_message) & 1:
        final_message += 'X'

    return final_message

def generate_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    # add key chars into the table 
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    # add remaining alphabet letters
    for char in alphabet:
        if char not in table:
            table.append(char)

    return table

def encrypt(message, key):
    table = generate_table(key)
    message = prepare_input(message)
    cipher = ""

    # build the table using the chunker which divides the message in parts with 2 letters each
    for char1, char2 in chunker(message, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
        # if letters are same on the row replace with the next right one 
        if row1 == row2:
            cipher += table[row1*5+(col1+1)%5]
            cipher += table[row2*5+(col2+1)%5]
        # if letters are some on the column replace with the next below one 
        elif col1 == col2:
            cipher += table[((row1+1)%5)*5+col1]
            cipher += table[((row2+1)%5)*5+col2]
        # if not the same replace with those from same row but other corner 
        else: 
            cipher += table[row1*5+col2]
            cipher += table[row2*5+col1]
    
    # print(table)
    return cipher


def decrypt(cipher, key):
    table = generate_table(key)
    decrypted = ""

    # build the table using the chunker which divides the message in parts with 2 letters each
    for char1, char2 in chunker(cipher, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
        # if letters are same on the row replace with the next left one 
        if row1 == row2:
            decrypted += table[row1*5+(col1-1)%5]
            decrypted += table[row2*5+(col2-1)%5]
        # if letters are some on the column replace with the next upper one    
        elif col1 == col2:
            decrypted += table[((row1-1)%5)*5+col1]
            decrypted += table[((row2-1)%5)*5+col2]
        # if not the same replace with those from same row but other corner 
        else: 
            decrypted += table[row1*5+col2]
            decrypted += table[row2*5+col1]

    return decrypted
    
def main():
    message = input('Enter text to be encrypted: ')
    key = input('Enter your key: ')

    cipher = encrypt(message, key)
    decrypted = decrypt(cipher, key)
    
    print("Your message: " + message)

    print("Encrypted message: " + cipher)

    print("Decrypted message: " + decrypted)


main()