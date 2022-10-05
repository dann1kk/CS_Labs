# Block Cipher

## Theory

&ensp;&ensp;&ensp; This is an implementation of the Blowfish cipher, which is a symmetric key cipher implementing permutation and
substitution boxes. These boxes are used to scramble a message during encryption and then unscramble it during
decryption.

## Implementation 
The functions used are __init__, encrypt, decrypt, __round_func, and cipher. __init__ is used to initialize the
permutation and substitution boxes using a given key. Encrypt will scramble a given 8 byte string. Decrypt will
unscramble the given encrypted string. __round_func is used as the round robin XOR on integers pertaining to the boxes.
Cipher is used to initialize the key made from the original key used for scrambling and unscrambling the message given.

*accepts only 8 byte blocks, but you can introduce two at the same time if you wish 

### Initial Steps:
&ensp;&ensp;&ensp; As for start can be considered the __init__, __round_func and cipher functions. 
__init__ being basically used to create an instance of blowfish and use key as encryption key. 

Cipher function being used for encrypting data, having two blocks (upper and lower) of 32-bits.

Round_func working with the same blocks of data and returning 32-bit result as a long integer

```
   # create instance of blowfish using key as encryption key
    def __init__ (self, key):

        # handler for incorrect key size
        if not key or len (key) < 8 or len (key) > 56:
            print("Key length must be between 8 and 56 bytes. Current key length: %s" %len (key))
            return

             # Cycle through the p-boxes and round-robin XOR the key with the p-boxes
        key_len = len (key)
        index = 0
        for i in range (len (self.p_boxes)):
            val = (ord (key[index % key_len]) << 24) + \
                  (ord (key[(index + 1) % key_len]) << 16) + \
                  (ord (key[(index + 2) % key_len]) << 8) + \
                   ord (key[(index + 3) % key_len])
            self.p_boxes[i] = self.p_boxes[i] ^ val
            index = index + 4

        # Variables used in chain replacing process
        l, r = 0, 0

        # Begin chain replacing the p-boxes
        for i in range (0, len (self.p_boxes), 2):
            l, r = self.cipher (l, r, self.ENCRYPT)
            self.p_boxes[i] = l
            self.p_boxes[i + 1] = r

        # Chain replace the s-boxes
        for i in range (len (self.s_boxes)):
            for j in range (0, len (self.s_boxes[i]), 2):
                l, r = self.cipher (l, r, self.ENCRYPT)
                self.s_boxes[i][j] = l
                self.s_boxes[i][j + 1] = r

    # encrypt block of data where xl is upper 32-bits and xr lower 32-bits
    # 'direction' is the direction to apply the cipher, ENCRYPT or DECRYPT
    def cipher (self, xl, xr, direction):
            # runs through xl and xr using the p-boxes to change the integers
            if direction == self.ENCRYPT:
                for i in range (16):
                    xl = xl ^ self.p_boxes[i]
                    xr = self.__round_func (xl) ^ xr
                    xl, xr = xr, xl
                xl, xr = xr, xl
                xr = xr ^ self.p_boxes[16]
                xl = xl ^ self.p_boxes[17]
            else:
                for i in range (17, 1, -1):
                    xl = xl ^ self.p_boxes[i]
                    xr = self.__round_func (xl) ^ xr
                    xl, xr = xr, xl
                xl, xr = xr, xl
                xr = xr ^ self.p_boxes[1]
                xl = xl ^ self.p_boxes[0]
            return xl, xr

    # function on 32-bit block from 'xl', which is the left half of the 64-bit block of data and return 32-bit result as a long integer
    def __round_func (self, xl):
        a = (xl & 0xFF000000) >> 24
        b = (xl & 0x00FF0000) >> 16
        c = (xl & 0x0000FF00) >> 8
        d = xl & 0x000000FF

        # Perform all ops as longs then and out the last 32-bits to obtain the integer
        f = (int (self.s_boxes[0][a]) + int (self.s_boxes[1][b])) % self.modu
        f = f ^ int (self.s_boxes[2][c])
        f = f + int (self.s_boxes[3][d])
        f = (f % self.modu) & 0xFFFFFFFF

        return f
```

### Encryption
&ensp;&ensp;&ensp;  At the encryption part we encrypt a 8-byte block of text, which should be 8 byte string and return encrypted string. For this, I use big endianness for the blocks of data xl and xr, which means I store the most significant byte of a word at the smallest memory address and the least significant byte at the largest.
```
 def encrypt (self, data):

        # handler for incorrect string length
        if not len (data) == 8:
            print("Encrypt block length is larger or smaller then the correct length of 8. Length: %s" %len (data))
            return ""

        # Using big endianness for the xl,xr encryption
        xl = ord (data[3]) | (ord (data[2]) << 8) | (ord (data[1]) << 16) | (ord (data[0]) << 24)
        xr = ord (data[7]) | (ord (data[6]) << 8) | (ord (data[5]) << 16) | (ord (data[4]) << 24)

        cl, cr = self.cipher (xl, xr, self.ENCRYPT)
        chars = ''.join ([
            chr ((cl >> 24) & 0xFF), chr ((cl >> 16) & 0xFF), chr ((cl >> 8) & 0xFF), chr (cl & 0xFF),
            chr ((cr >> 24) & 0xFF), chr ((cr >> 16) & 0xFF), chr ((cr >> 8) & 0xFF), chr (cr & 0xFF)
        ])
        return chars
```

### Decryption
&ensp;&ensp;&ensp; In the decryption I use the same method as in encryption, this time only in opposite 'direction'. 
```
def decrypt (self, data):

        # handler for incorrect string length
        if not len (data) == 8:
            print("Decrypt block length is larger or smaller then the correct length of 8. Length: %s" %len (data))
            return ""

        # Using big endianness for the xl,xr encryption same as above
        cl = ord (data[3]) | (ord (data[2]) << 8) | (ord (data[1]) << 16) | (ord (data[0]) << 24)
        cr = ord (data[7]) | (ord (data[6]) << 8) | (ord (data[5]) << 16) | (ord (data[4]) << 24)

        xl, xr = self.cipher (cl, cr, self.DECRYPT)
        chars = bytes ([
            ((xl >> 24) & 0xFF), ((xl >> 16) & 0xFF), ((xl >> 8) & 0xFF), (xl & 0xFF),
            ((xr >> 24) & 0xFF), ((xr >> 16) & 0xFF), ((xr >> 8) & 0xFF), (xr & 0xFF)
        ])
        return chars
```

## Screenshots
![](https://github.com/dann1kk/CS_Labs/blob/main/Resources/block.png)