import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "fototeste.jpg"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = "testando123"
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file_name = "fototeste.jpg"
new_file = open(nem_file_name,"wb")
new_file.write(crypto_data)
new_file.close()