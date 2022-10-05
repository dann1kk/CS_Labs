import random

def randomKey(): #random key generator
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~" #ascii collection
    a = random.randint(1,9) #random multiplier
    c = random.randint(1,9) #random counter
    s = 1
    m = int(len(alphaCollection)) #modulo the length of alphaCollection 
    result = "" #store the new key

    #LCG pseudo random number algorithm
    for i in range(s, 9):
        randomNum = (s*a+c) % m
        s = randomNum
        result += alphaCollection[s]
    return result

def encrypt(text, key):
    #ascii collection
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~ "
    #add the new key length depending on how many characters are in the message.
    new_key = key 
    # Pointer counter
    i = 0 
    # Store the encrypted message
    result = "" 
    # if the length of the key is not equal to the message lenght: run this until it matches the same length
    while len(new_key) < len(text):
    #add the characters based on the index number provided in i variable    
        new_key = new_key + key[i] 
    # increment i variable by 1 and modulo the lenght of the key to reset the number to 0 if reached the last character. Avoiding index error
        i = (i + 1) % len(key) 
    # for each character in text and new_key run this
    for alpha, alphaKey in zip(text, new_key):
    # find the index position of the each character in text and newkey, add them together and modulo the lenght of alphaCollection:
        newLetterindex = (alphaCollection.index(alpha) + alphaCollection.index(alphaKey)) % int(len(alphaCollection))
    # add the characters found in alphaCollection based on the number newLetterindex provided.  
        result += alphaCollection[newLetterindex]
    return result


def decrypt(text, key):
    #ascii collection
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~ "
    #add the new key length depending on how many characters are in the message.
    new_key = key 
    # Pointer counter
    i = 0 
    # Store the encrypted message
    result = "" 
    # if the length of the key is not equal to the message lenght: run this until it matches the same length
    while len(new_key) < len(text):
    #add the characters based on the index number provided in i variable    
        new_key = new_key + key[i] 
    # increment i variable by 1 and modulo the lenght of the key to reset the number to 0 if reached the last character. Avoiding index error
        i = (i + 1) % len(key) 
    # for each character in text and new_key run this
    for alpha, alphaKey in zip(text, new_key):
    # find the index position of the each character in text and newkey, add them together and modulo the lenght of alphaCollection:
        newLetterindex = (alphaCollection.index(alpha) - alphaCollection.index(alphaKey)) % int(len(alphaCollection))
    # add the characters found in alphaCollection based on the number newLetterindex provided.  
        result += alphaCollection[newLetterindex]
    return result



# def main():
#     message = input("Enter a message: ")
#     newKey = randomKey()
#     print("Your new key is: ", newKey)

#     for i in range(2):
#         encryption = encrypt(message, newKey)
#         res = encrypt(encryption, newKey)
#     print("Encrypted message is: " + res)

#     for i in range(2):
#         decryption = decrypt(res, newKey)
#         res2 = decrypt(decryption, newKey)
#     print("Decrypted message is:" + res2)

# main()