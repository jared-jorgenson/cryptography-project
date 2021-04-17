import string


def atbash_encrypt(secret):
    # Create variables for the function
    letters_list = list(string.ascii_lowercase)
    reverse_list = letters_list[::-1]
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
            encryption_list.append(reverse_list[secret_list[x]])

    # Change the encrypted list into a string
    encryption = "".join(encryption_list)
    return encryption


def atbash_decrypt(encrypted_secret):
    # Since the atbash function reverses itself we simplify the
    # decryption function as simply re-using the encryption function 
    # on the encryption
    decryption = atbash_encrypt(encrypted_secret)
    return decryption
