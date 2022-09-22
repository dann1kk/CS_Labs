# Caesar Substitution Cipher

## Theory

&ensp;&ensp;&ensp; It's one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 

&ensp;&ensp;&ensp;  For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

## Implementation 

### Initial Step 
&ensp;&ensp;&ensp; Make an initial mapping using dictionaries between letters in alphabet and their corresponding indexes.
```
 # dictionary for mapping between alphabet letter and index, ex. a => 0, b => 1 ... 
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    # an inverse mapping between index and letter 
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))
```

### Encryption

&ensp;&ensp;&ensp;  At the encryption part we use dictionaries which are mapping letters in the alphabet and their indexes.
In this way, when we make a shift we simply deduce the letter by checking it new index and replacing it with the new corresponding letter. 
```
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
```

### Decryption

&ensp;&ensp;&ensp; Same dictionaries are used but this time we perform a shift back.

```
def decrypt(cipher, shift, letter_to_index, index_to_letter):
    decrypted = ""

    for letter in cipher:
        # same as in encryption, just take back the shift and do modulo of alphabet size
        number = (letter_to_index[letter] - shift) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted
```

## Screenshots

![](https://github.com/dann1kk/CS_Labs/blob/main/Laboratory_Work_1/Screenshots/Caesar_Subsitution.png)
