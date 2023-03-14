### Sprint 3

    1. Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
        ~~~
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        print(100-idade+2023)
        ~~~

    2. Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).
    Importante: Aplique a função range() em seu código.
    Exemplos de saída: Par: 2; Ímpar: 3
        ~~~
        for i in range(1,4):
        numero = int(input("Digite o numero: "))
            if (numero%2==0):
        print("Par:",numero)
            else:
        print("Ímpar:",numero)
        ~~~

    3. Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).
    Importante: Aplique a função range() em seu código.
        ~~~
        start = 0
            x = range(start, 22, 2)

            for n in x:
        print(n)
        ~~~

    4. Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não. Importante: Aplique a função range().
        ~~~
        start = 1
        end = 100
  
        for i in range(start, end+1): 
            if i>1: 
        for n in range(2,i): 
            if(i % n==0): 
                break
            else: 
        print(i) 
        ~~~

    5. Escreva um código Python que declara 3 variáveis:
        dia, inicializada com valor 22
        mes, inicializada com valor 10 e
        ano, inicializada com valor 2022
    Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.
        ~~~
        dia = 22
        mes = 10
        ano = 2022

        print(f'{dia}/{mes}/{ano}')
        ~~~
