### Sprint 3

    6. Considere as duas listas abaixo:
    a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores da interseção na saída padrão.
        ~~~
        a = [1,1,2,3,5,8,14,21,34,55,89]
        b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        i = [numero for numero in a if numero in b]
        print (sorted(set(i)))
        ~~~

    7.Dada a seguinte lista:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    Faça um programa que gere uma nova lista contendo apenas números ímpares.
        ~~~
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista2 = []
for valor in a:
    if valor % 2 != 0:
        lista2.append(valor)

print(lista2)
        ~~~

    8.Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
    Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
    É necessário que você imprima no console exatamente assim:
        A palavra: maça não é um palíndromo
        A palavra: arara é um palíndromo
        A palavra: audio não é um palíndromo
        A palavra: radio não é um palíndromo
        A palavra: radar é um palíndromo
        A palavra: moto não é um palíndromo
        ~~~
list = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for word in list:
    palindromo = True
    start = 0
    end = len(word) - 1  

    while start < end:
        if word[start] != word[end]:
            print(f"A palavra: {word} não é um palíndromo")
            palindromo = False
            break
        start = start + 1
        end = end - 1

    if palindromo:
        print(f"A palavra: {word} é um palíndromo")
        ~~~

    9. Dada as listas a seguir:
    primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
    sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
    idades = [19, 28, 25, 31]
    Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
    Exemplo:
    0 - João Soares está com 19 anos
        ~~~
        primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
        sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
        idades = [19, 28, 25, 31]

    for i, v in enumerate(primeirosNomes):
        pN = primeirosNomes[i]
        sN = sobreNomes[i]
        iD = idades[i]
        print(f"{i} - {pN} {sN} está com {iD} anos")
        ~~~

    10. Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.
    ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
        ~~~
        lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
        print(sorted(set(lista)))
        ~~~

    11. Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
    Dica: leia a documentação da função open(...)
    ~~~
    arquivo = open('arquivo_texto.txt')
texto = arquivo.read()
print(texto, end=(""))
    ~~~

    12. Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
    Dica: leia a documentação do pacote json
    ~~~
    import json

with open('person.json', 'r') as file:
    data = json.load(file)
    print(data)
    ~~~

    13. Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
    Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
    ~~~
    def my_map(list, f):
    return [f(x) for x in list]
def potencia_de_2(x):
    return x ** 2

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = my_map(lista_original, potencia_de_2)
print(nova_lista)
    ~~~

    14. Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
    Teste sua função com os seguintes parâmetros:
    (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

    15. Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
    liga(): muda o estado da lâmpada para ligada
    desliga(): muda o estado da lâmpada para desligada
    esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
    Para testar sua classe:
    Ligue a Lampada
    Imprima: A lâmpada está ligada? True
    Desligue a Lampada
    Imprima: A lâmpada ainda está ligada? False
    ~~~
    class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
        
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada

lampada = Lampada(True)
lampada.liga()
print("A lâmpada está ligada?", lampada.esta_ligada())
lampada.desliga()
print("A lâmpada ainda está ligada?", 				   
lampada.esta_ligada())
    ~~~

    16. Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.
    A string deve ter valor  "1,3,4,6,10,76"
    ~~~
    def soma_num_string(string_numeros):
    numeros = string_numeros.split(',')
    soma = 0
    for num in numeros:
        soma += int(num)
    return soma
string_numeros = "1,3,4,6,10,76"
soma = soma_num_string(string_numeros)
print(soma)
    ~~~

    17. Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ~~~
    def dividir_lista(lista):
    tamanho_parte = len(lista) // 3
    partes = [lista[i:i+tamanho_parte] for i in range(0, len(lista), tamanho_parte)]
    return tuple(partes)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
partes = dividir_lista(lista)
print(partes)
    ~~~

    18. Dado o dicionário a seguir:
    speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
    Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.
    ~~~
    speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

lista_valores = list(set(speed.values()))

print(lista_valores)
    ~~~

    19. Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
    Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
    import random
    amostra aleatoriamente 50 números do intervalo 0...500
    random_list = random.sample(range(500),50)
    Use as variáveis abaixo para representar cada operação matemática
    mediana
    media
    valor_minimo
    valor_maximo
    ~~~
    import random 

#amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list)/len(random_list)

sorted_list = sorted(random_list)
tamanho = len(sorted_list)
meio = tamanho // 2

if tamanho % 2 == 0:
    mediana = (sorted_list[meio - 1] + sorted_list[meio]) / 2
else:
    mediana = sorted_list[meio]

print("Media: {}, Mediana: {}, Mínimo: {}, Máximo: {}".format(media, mediana, valor_minimo, valor_maximo))
    ~~~

    20. Imprima a lista abaixo de trás para frente.
    a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        ~~~
        a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        myinput = a[::-1]
        print(myinput)
        ~~~
