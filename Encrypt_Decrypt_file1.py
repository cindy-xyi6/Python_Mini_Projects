import os
curr_dir = os.getcwd()
target_dir = "C:/Users/cindy/Documents/Python/coding_python"
os.chdir(target_dir)
print(os.getcwd())

###################################################################

#read (encrypt_file1.txt)
file = open("encrypt_file1.txt", "r")
information = str(file.read())
#changing characters into a list.
info = list(information)
# print(info)
# converting characters into ascii values
Hej_ascii_values = []
index = 0 
for x in info:
    info_letter = info[index]
    letter_ascii = ord(info_letter)
    # ord converts letters into ascii values
    Hej_ascii_values.append(letter_ascii)
    # print(letter_ascii)
    index += 1

# print(Hej_ascii_values)

###################################################################
#Encrypt
import string
import random
num_for_encrypt = random.randint(0,26)
# print(num_for_encrypt)

###########################################################################################
#tokenizing
index = 0
encrypt_index = []
for x in range(len(information)):
    ascii_num = Hej_ascii_values[index]
    if (ascii_num == 10):
        encrypt_index.append(10)
        # leaves the eol(end of line) ascii value alone.
    else:
        new_letter_num = (ascii_num + num_for_encrypt)
# using ascii value range 127.
        if (new_letter_num > 127):
            equ = (new_letter_num - 97)
            #-97 so value does not go below 32, so other symbols arent included.
            encrypt_index.append(equ)
        else:
            encrypt_index.append(new_letter_num)

        # print(encrypt_index)
    index +=1
# print(encrypt_index)
#get the index of the 1 letter in the alphabet_list
#add the number [num_for_encrypt] to the index
#change indexs into letters

###############################################################################################
#changing ascii into letter 
encrypted = ""
for num in encrypt_index:
    encrypted = encrypted + chr(num)
#     print(index)
# print(letter)

print("Encryption: " + str(encrypted))

# Encryption = (information)
file.close()
# writing encrypt into text file.
file = open("encrypt_file1.txt", "w")
file.write(encrypted)
file.close()

##################################################################################
#Decrypt
file = open("encrypt_file1.txt", "r")
decrypting = str(file.read())
num_for_decrypt = num_for_encrypt

def decrypt(text):
    #turns text into a list
    encrypted_characters = list(text) 
    # print(text_list)
    decrypt_txt = []
#converts characters into ascii values
    index = 0 
    for x in info:
        decrypt_letter = encrypted_characters[index]
        decrypt_ascii = ord(decrypt_letter)
        decrypt_txt.append(decrypt_ascii)
    # print(letter_ascii)
        index += 1

    index = 0
    decrypt_value= []
    for x in range(len(text)):
        decrypt_ascii = decrypt_txt[index]
        if (decrypt_ascii == 10):
            #leaves eol value alone.
            decrypt_value.append(10)
        else:
            decrypt_text = (decrypt_ascii - num_for_decrypt)

            if (decrypt_text < 32):
                equ = (decrypt_text + 97)
                decrypt_value.append(equ)
            else: 
                decrypt_value.append(decrypt_text)
        index +=1
    # print(decrypt_index)

######################################################################################
# turns it back into a letter 
    #changing ascii into letter 
    decrypted = ""
    for number in decrypt_value:
        decrypted = decrypted + chr(number)
        # print(index)
    # print(letter)
    print("Decryption: " + "Go to encrypt_file1.txt")

    # print("Decryption: " + str(decrypted))

    file = open("encrypt_file1.txt", "w")
    file.write(decrypted)
    file.close()

# Encryption = (information)

Decryption = decrypt(decrypting)
