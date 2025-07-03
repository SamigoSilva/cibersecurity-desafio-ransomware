from Crypto.Cipher import AES
import os

def encrypt_file(key, file_path):
    # Implementação da criptografia AES
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    # Sobrescreve o arquivo original
    with open(file_path, 'wb') as f:
        [ f.write(x) for x in (cipher.nonce, tag, ciphertext) ]
