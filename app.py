from ceaser_cipher import ceaser_encrypt, ceaser_decrypt

right_rotataion = 10

secret_encrypted = ceaser_encrypt("python is pretty cool", right_rotataion)
secret_decrypted = ceaser_decrypt(secret_encrypted, right_rotataion)

print(secret_encrypted)
print(secret_decrypted)
