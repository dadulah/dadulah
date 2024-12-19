import random 
import string

chars = string.punctuation + string.digits + " " + string.ascii_letters 
 
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"Key: {key}")

#ENCRYPT
print("---------------  ENCRYPT  -------------------")
plain_text = input("Enter a massage to encrypt: ")
cipher_text = ""


for letter in plain_text:
  index = chars.index(letter)
  cipher_text += key[index]

print(f"Massage is encrypted to : {cipher_text}")
print()

print("---------------  DECRYPT  -------------------")
if input("Want to decrypt the massage (y/n)?: ") == "y":
  cipher_text = input("Enter a massag to decrypt: ")
  original_text = ""

  for letter in cipher_text:
    index = key.index(letter)
    original_text += chars[index]

  print(f"Original massage is: {original_text}")
  
print("Have good day!")
print()

#my_chars = list(my_chars) + ".COM" + ".IR" + ".ONION" + ".DEV"
# my_chars = string.digits + string.ascii_lowercase