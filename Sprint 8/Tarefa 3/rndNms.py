import random
import time
import os
import names
import csv

# [Warm up] Lista reversa de 250 inteiros aleatórios

random_integers = [random.randint(1, 100) for _ in range(250)]
random_integers.reverse()
print(random_integers)

# [Warm up] 20 nomes de animais

animal_names = ["Elefante", "Tigre", "Leão", "Girafa", "Zebra", "Macaco", "Urso", "Hipopótamo", "Rinoceronte", "Canguru",
                "Cobra", "Panda", "Pinguim", "Jacaré", "Arara", "Cachorro", "Camelo", "Lobo", "Raposa", "Falcão"]

sorted_animal_names = sorted(animal_names)
[print(animal) for animal in sorted_animal_names]

# Salvando o nome dos animais em CSV

filename = "animal_names.csv"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows([[animal] for animal in sorted_animal_names])

print(f"Animal names saved to {filename}")

# [Laboratório] Gerando dataset de nomes aleatórios

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Generating {qtd_nomes_aleatorios} random names")

dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

# Salvando os nomes aleatórios em um arquivo .txt

filename = "nomes_aleatorios.txt"
with open(filename, "w") as file:
    file.write("\n".join(dados))

print(f"Random names saved to {filename}")

# Checando o conteúdo do arquivo criado
os.system(f"notepad.exe {filename}")
os.system(f"vim {filename}")
