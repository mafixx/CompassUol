# Exercício 4

# A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.
# Veja o exemplo:

# Entrada
# operadores = ['+','-','*','/','+']
# operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

# Aplicar as operações aos pares de operandos
# [ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 

# Obter o maior dos valores
# 12

# Na resolução da atividade você deverá aplicar as seguintes funções:
# max
# zip
# map

def calcular_valor_maximo(operadores, operandos):
    # Dicionário que mapeia cada operador para a sua respectiva operação matemática
    operacoes = {'+': lambda a, b: a+b,
                 '-': lambda a, b: a-b,
                 '*': lambda a, b: a*b,
                 '/': lambda a, b: a/b,
                 '%': lambda a, b: a%b}
    # Aplica as operações aos pares de operandos utilizando a função map
    resultados = list(map(lambda op: operacoes[op[0]](op[1][0], op[1][1]), zip(operadores, operandos)))
    # Retorna o maior valor dos resultados usando max
    return max(resultados)
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)