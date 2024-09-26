import string

chars = "abcdefghijklmnñopqrstuvwxyz"
displacement = 4

#Decrypt
encrypted_text = input("Input your Crypted message to Decrypt: ")
print("")
decrypt_text = ""

for letter in encrypted_text:
    if letter in chars:
        index = chars.index(letter)
        decrypt_text += chars[(index - displacement) % len(chars)]  #Cipher Algorithm
    else:
        decrypt_text += letter

print("Crypted Message: " + encrypted_text)
print("")
print("Decrypted Message: " + decrypt_text)
