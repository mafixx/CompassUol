# Script em Python
import hashlib

while True:
    # Recebe a string via input
    input_str = input("Digite uma string: ")

    # Gera o hash SHA-1
    sha1_hash = hashlib.sha1(input_str.encode())

    # Imprime o hash em tela, utilizando o método hexdigest
    print(f"O hash da string '{input_str}' é: {sha1_hash.hexdigest()}")
