import string


def ceaser_encrypt(secret, n="right rotation"):
    # Set variables for the function
    letters_list = list(string.ascii_lowercase)
    secret = secret.lower()
    ceasar_list = []
    secret_list = []
    encryption_list = []

    # Create a list of the alphabet with new cipher indices
    [ceasar_list.append(letters_list[(x + n) % 26]) for x in range(26)]

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
            encryption_list.append(ceasar_list[secret_list[x]])

    # Change the encrypted list into a string
    encryption = "".join(encryption_list)
    return encryption


def ceaser_decrypt(encryption, n="left rotation"):
    # Set variables for the function
    letters_list = list(string.ascii_lowercase)
    encryption = encryption.lower()
    ceasar_list = []
    encryption_list = []
    decryption_list = []

    # Create a list of the alphabet with the decryption indices
    [ceasar_list.append(letters_list[(x - n) % 26]) for x in range(26)]

    # Replace the encrypted message with a list of numbers that correspond
    # to the indices of the letters in the encrypted message
    for x in range(0, len(encryption)):
        if encryption[x] not in letters_list:
            encryption_list.append(encryption[x])
        else:
            encryption_list.append(ord(encryption[x]) - 97)

    # Replace the numbers in the list created above with the decryption indices
    # & then replace those indices with the decryption letters
    for x in range(0, len(encryption_list)):
        if type(encryption_list[x]) != int:
            decryption_list.append(encryption_list[x])
        else:
            decryption_list.append(ceasar_list[encryption_list[x]])

    # Change the decrypted list into a string
    decryption = "".join(decryption_list)
    return decryption

