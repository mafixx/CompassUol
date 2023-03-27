# Exercício 1

# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.

# Você deverá aplicar as seguintes funções no exercício:

#map
#filter
#sorted
#sum

# Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):

# a lista dos 5 maiores números pares em ordem decrescente;

# a soma destes valores.

with open("number.txt") as file:
    numbers = list(map(int, file.readlines()))
    
pairs = list(filter(lambda y: y % 2 == 0, numbers)) # O certo era o console exibir com o set, já que o list não pega o valor com final 92 e sim, repete o penúltimo
great_pairs = sorted(pairs, reverse=True)[:5]
sum_great_pairs = sum(great_pairs)

print(great_pairs)
print(sum_great_pairs)