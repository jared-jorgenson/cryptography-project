import string
import random


def sub_encrypt(secret):
    # Set variables for the function
    letters_list = list(string.ascii_lowercase)
    random_list = random.sample(letters_list, len(letters_list))
    secret = secret.lower()
    secret_list = []
    encryption_list = []

    # Replace the secret message with a list of numbers that correspond
    # to the indices of the letters in the secret message
    for x in range(0, len(secret)):
        if secret[x] not in letters_list:
            secret_list.append(secret[x])
        else:
            secret_list.append(ord(secret[x]) - 97)

    # Replace the numbers in the list created above with the ciphers indices
    # and then replace those indices with the ciphers letters
    for x in range(0, len(secret_list)):
        if type(secret_list[x]) != int:
            encryption_list.append(secret_list[x])
        else:
            encryption_list.append(random_list[secret_list[x]])

    # Change the encrypted list into a string
    # Return the random cipher key so it can be decrypted
    encryption = "".join(encryption_list)
    random_cipher = "".join(random_list)

    return encryption, random_cipher


def sub_decrypt(encrypted_secret, cipher_key):
    # Set variables for the function
    letters_list = list(string.ascii_lowercase)
    key_list = list(cipher_key)
    encrypted_secret = encrypted_secret.lower()
    encrypted_list = []
    decryption_list = []

    # Replace the encrypted message with a list of numbers that correspond
    # to the indices in the cipher key list
    for x in range(0, len(encrypted_secret)):
        if encrypted_secret[x] not in letters_list:
            encrypted_list.append(encrypted_secret[x])
        else:
            encrypted_list.append(key_list.index(encrypted_secret[x]))

    # Replace the numbers in the list created above with the standard
    # alphabet indices and then switch these to letters
    for x in range(0, len(encrypted_list)):
        if type(encrypted_list[x]) != int:
            decryption_list.append(encrypted_list[x])
        else:
            decryption_list.append(letters_list[encrypted_list[x]])

    # Change the decrypted list into a string
    decryption = "".join(decryption_list)

    return decryption
