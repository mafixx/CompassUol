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
