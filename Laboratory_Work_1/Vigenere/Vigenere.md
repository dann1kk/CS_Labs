# Vigenere Cipher

## Theory
&ensp;&ensp;&ensp; The Vigenère cipher is a polyalphabetic substitution cipher that is a natural evolution of the Caesar cipher. The Caesar cipher encrypts by shifting each letter in the plaintext up or down a certain number of places in the alphabet. If the message was right shifted by 4, each A would become E, and each S would become W.

&ensp;&ensp;&ensp; In the Vigenère cipher, a message is encrypted using a secret key, as well as an encryption table (called a Vigenere square, Vigenere table, or tabula recta). The tabula recta typically contains the 26 letters of the Latin alphabet from A to Z along the top of each column, and repeated along the left side at the beginning of each row. Each row of the square has the 26 letters of the Latin alphabet, shifted one position to the right in a cyclic way as the rows progress downwards. Once B moves to the front, A moves down to the end. This continues for the entire square.

## Implementation 

### Initial Step 
&ensp;&ensp;&ensp; Make an initial mapping using dictionaries between letters in alphabet and corresponding indexes.
```
 # dictionary for mapping between alphabet letter and index, ex. a => 0, b => 1 ... 
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    # an inverse mapping between index and letter 
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))
```

#### Encryption 
&ensp;&ensp;&ensp;  In encryption and decryption we use the same mapping between letters and indexes.
```
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
```

### Decryption 

```
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
```

## Screenshots 
![](https://github.com/dann1kk/CS_Labs/blob/main/Laboratory_Work_1/Screenshots/Vigenere.png)
