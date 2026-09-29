import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters # this shows all the valid characters which are allowed
chars = list(chars) # type casted the chars in to a list as an individual element

key = chars.copy() # key is the copy of the same chars list
random.shuffle(key) # this will shuffle the key order everytime ( lets say that chars[3] = A so key[3] = ? etc)

#ENCRYPTION 

plain_text = input("Enter Message = ") # enter message in plain language
cipher_text = "" # this will contain the encrypted messsage , intially empty

for letter in plain_text: # for every letter in plain language
    index = chars.index(letter) # look for the index of that letter in the chars list
    cipher_text += key[index] # then look for the same index in the key and store it in the cipher text variable

print(f"ORIGINAL = {plain_text}") # print the original plain text 
print(f"ENCRYPTED = {cipher_text}") # encrypted version

#DECRYPTION

cipher_text = input("Enter Encrypted = ") # enter encrypted messgae
plain_text = "" # plain text is empty

for letter in cipher_text: # for every letter in encrypted version
    index = key.index(letter) # look for its index in the key
    plain_text += chars[index] # look for the same index in the chars list

print(f"ENCRYPTED = {cipher_text}") # show the encrypted message
print(f"ORIGINAL = {plain_text}") # convert to plain language
