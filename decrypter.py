from Crypto.Cipher import AES
import os

def decrypt_file(key, file_path):
    # Implementação da descriptografia
    with open(file_path, 'rb') as f:
        nonce, tag, ciphertext = [ f.read(x) for x in (16, 16, -1) ]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    # Restaura o arquivo original
    with open(file_path, 'wb') as f:
        f.write(data)
