# Caesar Permutation Cipher

## Theory

&ensp;&ensp;&ensp; It is a type of mono-alphabetic permutation cipher where the letters of the alphabet are arranged based on a given key.


## Implementation 

### Initial Step 
&ensp;&ensp;&ensp; Make an initial mapping using dictionaries between letters in alphabet and corresponding indexes.
```
 # dictionary for mapping between alphabet letter and index, ex. a => 0, b => 1 ... 
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    # an inverse mapping between index and letter 
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))
```
### Alphabet Generation

&ensp;&ensp;&ensp; Add at start only unique characters from the message, afterwards all the remaining alphabet letters.
```
# create new alphabet 
    alphabet = []
    all_alphabet_letters = string.ascii_lowercase
    # add all unique characters from message
    for character in key:
        if character not in alphabet:
            alphabet += character 
    # add remaining alphabet letters
    for i in all_alphabet_letters:
        if i not in alphabet:
            alphabet.append(i)  
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
![](https://github.com/dann1kk/CS_Labs/blob/main/Resources/Caesar_Permutation.png)