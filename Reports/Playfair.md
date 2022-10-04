# Playfair Cipher

## Theory
&ensp;&ensp;&ensp; 
The Playfair cipher uses a 5 by 5 table containing a key word or phrase. Memorization of the keyword and 4 simple rules was all that was required to create the 5 by 5 table and use the cipher.

&ensp;&ensp;&ensp;  To generate the key table, one would first fill in the spaces in the table (a modified Polybius square) with the letters of the keyword (dropping any duplicate letters), then fill the remaining spaces with the rest of the letters of the alphabet in order (usually omitting "J" or "Q" to reduce the alphabet to fit; other versions put both "I" and "J" in the same space). 

&ensp;&ensp;&ensp;  The key can be written in the top rows of the table, from left to right, or in some other pattern, such as a spiral beginning in the upper-left-hand corner and ending in the center. The keyword together with the conventions for filling in the 5 by 5 table constitute the cipher key.

## Implementation
### Initial Steps 

1. Create a function chunker which will basically split our message in small parts, 2 letters each.

2. Prepare input by converting it to uppercase and separating repeated letters with 'X'

3. Generate the table with key chars and remaining alphabet letters 

```
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
```

## Encryption 
&ensp;&ensp;&ensp;  At the encryption we follow 3 rules: 
1. If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively
2. If the letters appear on the same column of your table, replace them with the letters immediately below respectively
3. If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle
```
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
```

## Decryption 
&ensp;&ensp;&ensp; Same rules are followed in decryption. But, we do the inverse (opposite) of the two shift rules, selecting the letter to the left or upwards as appropriate, the last rule remains the same.
```
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
```

## Screenshots
![](https://github.com/dann1kk/CS_Labs/blob/main/Resources/Playfair.png)