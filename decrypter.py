import os
import pyaes

## abrir o arquivo criptografado
file_name = "fototeste.jpg"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = "testando123"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "fototeste.jpg"
new_file = open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()