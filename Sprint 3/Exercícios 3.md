### Sprint 3

    1. Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.

Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
~~~python
class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        pass


class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")
        
pato = Pato()
print("Pato")
pato.voar()
pato.emitir_som()

pardal = Pardal()
print("Pardal")
pardal.voar()
pardal.emitir_som()
~~~

    2. Crie uma classe chamada "Pessoa" com um atributo privado "nome" (representado como "__nome") e um atributo público "id". Adicione duas funções à classe, uma para definir o valor de "nome" e outra para obter o valor de "nome". Observe que o atributo "nome" deve ser privado e acessado somente através dessas funções.

Para testar seu código use:

pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
~~~python
class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None
        
    def set_nome(self, nome):
        self.__nome__ = nome
        
    def nome(self):
        return self.__nome
        
pessoa = Pessoa(0)
pessoa.nome = "Fulano de Tal"
print(pessoa.nome)
~~~

    3. Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:

x = 4 
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1
~~~python
class Calculo:
    def __init__(self):
        pass
    
    def soma(self, x, y):
        return x + y
        
    def subtracao(self, x, y):
        return x - y

x = 4
y = 5
calculo = Calculo()
print(f'Somando: {x}+{y} = {calculo.soma(x,y)}')
print(f'Subtraindo: {x}+{y} = {calculo.subtracao(x,y)}')
~~~

    4. Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.
    Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8]. 
    Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método
    ordenacaoDecrescente.

Imprima o resultado da ordenação crescente e da ordenação decresce

[1, 2, 3, 4, 5] 
[9, 8, 7, 6]
~~~python
class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())
~~~

    5. Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
    
    Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.
    
    Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
    
    Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
    
    “O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.
    Sendo x, y, z e w cada um dos atributos da classe “Avião”.
    
    Valores de entrada:

    modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul

    modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul

    modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul
~~~python

~~~