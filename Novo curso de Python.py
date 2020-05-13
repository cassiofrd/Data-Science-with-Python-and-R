# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:06:22 2020

@author: Cássio
"""

#Novo curso de Python
#while
i=0
while i<5:
    print(i)
    i+=1
#o comando breakinterrompe um loop imediatamente, de modo que o restante do código
#não fará parte do loop
i=0
lista=[0,1,2,3,4,10]

while i<len(lista):
    if lista[i]==10:
        break
    elif lista[i]!=10:
        i+=1
else: lista.append(10)
#encontrar o primeiro múltiplo de 7 em uma sequência
for i in range(1,10):
    if i%7==0:
        print("Encontrei")
        break
    else: pass
#é possível separar tuplas dentros de listas ou listas dentro de listas fazendo
#um for com dois termos, i e j
for i in [[1,2],[3,4]]:
    print(i)
for i,j in [[1,2],[3,4]]:
    print(i,j)
#olha só que maneira interessante de plotar o elemento de uma lista e seu índice
lista1=[1,2,3,10,'a','b','c']
for i in range(len(lista1)):
    print(i,lista1[i])    
#a classe me permite introduzir vários métodos
class circulo:
    def __init__(self,raio):#aqui eu vou definir as variáveis utilizadas para fazer os métodos
        self.raio=raio
    def area(self):
        return 'A área desse círculo é {0}'.format(3.14*(self.raio**2))
#podemos inserir métodos do python na nossa classe, como é o caso do método
#str, que transforma em string
class circulo:
    def __init__(self,raio):#aqui eu vou definir as variáveis utilizadas para fazer os métodos
        self.raio=raio
        self.area=3.14*(self.raio**2)
    def area(self):
        return 'A área desse círculo é {0}'.format(self.area)
    def __str__(self):
        return str(self.area)
#um método interessante é o __repr__, é a informação contida nele que aparece
#quando apenas selecionamos enter em um objeto de eterminada classe
class circulo:
    def __init__(self,raio):#aqui eu vou definir as variáveis utilizadas para fazer os métodos
        self.raio=raio
        self.area=3.14*(self.raio**2)
    def area(self):
        return 'A área desse círculo é {0}'.format(self.area)
    def __str__(self):
        return str(self.area)
    def __repr__(self):
        return 'Círculo de raio {0}, area {1} e volume {2}'.format(self.raio,self.area,4*3.14*(1/3)*(self.raio**2))
#para que dois objetos sejam comparáveis em termos de valores, devemos utilizar o método
#__eq__, e especificar as condições nas quais dois objetos de uma mesma classe
#possam ser definidos como iguais
#é importante acrescentar também a função isinstance para garantir que os dois
#objetos comparados são da mesma classe, circulos
class circulo:
    def __init__(self,raio):#aqui eu vou definir as variáveis utilizadas para fazer os métodos
        self.raio=raio
        self.area=3.14*(self.raio**2)
    def area(self):
        return 'A área desse círculo é {0}'.format(self.area)
    def __str__(self):
        return str(self.area)
    def __repr__(self):
        return 'Círculo de raio {0}, area {1} e volume {2}'.format(self.raio,self.area,4*3.14*(1/3)*(self.raio**2))
    def __eq__(self,other):
        if isinstance(other,circulo):
            return self.raio==other.raio
        else: False
#para além do igual, podemos acrescentar outros métodos, como __ls__ para menor
class circulo:
    def __init__(self,raio):#aqui eu vou definir as variáveis utilizadas para fazer os métodos
        self.raio=raio
        self.area=3.14*(self.raio**2)
    def area(self):
        return 'A área desse círculo é {0}'.format(self.area)
    def __str__(self):
        return str(self.area)
    def __repr__(self):
        return 'Círculo de raio {0}, area {1} e volume {2}'.format(self.raio,self.area,4*3.14*(1/3)*(self.raio**2))
    def __eq__(self,other):
        if isinstance(other,circulo):
            return self.raio==other.raio
        else: False
    def __eq__(self,other):
        if isinstance(other,circulo):
            return self.raio==other.raio
        else: False
    def __lt__(self,other):
        if isinstance(other, circulo):
            return self.raio<other.raio
        else: False
#podemos utilizaro  método set para limitar os valoresque podem ser atribuídos
#à nossa classe
class circulo:
    def __init__(self,raio):#aqui eu vou definir as variáveis utilizadas para fazer os métodos
        self.raio=raio
        self.area=3.14*(self.raio**2)
    def set_raio(self,raio):
        if raio<=0:
            raise ValueError('Existe círculo com raio que não seja positivo por um acaso?')
        else:
            self.raio=raio
    def area(self):
        return 'A área desse círculo é {0}'.format(self.area)
    def __str__(self):
        return str(self.area)
    def __repr__(self):
        return 'Círculo de raio {0}, area {1} e volume {2}'.format(self.raio,self.area,4*3.14*(1/3)*(self.raio**2))
    def __eq__(self,other):
        if isinstance(other,circulo):
            return self.raio==other.raio
        else: False
    def __eq__(self,other):
        if isinstance(other,circulo):
            return self.raio==other.raio
        else: False
    def __lt__(self,other):
        if isinstance(other, circulo):
            return self.raio<other.raio
        else: False
#objetos imutáveis em python são aqueles para os quais não há como modificar a
#posição na memória na qual ela faz referência, se mudamos são valor eles passam
#a fazer referência a outra posição na memória; números e strings são imutáveis
numero=1.5
id(numero)
numero=2
id(numero) #mudou o valor, mudou a posiçaõ na memória
#os objetos mutáveis são aqueles que podemos mudar sem que a posição na memória
#seja modificada, exemplo são as listas
lista=[1,2,3]
id(lista)
lista.append(4)
id(lista) #a lista mudou mas aposição na memória é a mesma
#as tuplas são imutáveis (não é possível mudar sem mudar a posição na memória)
#mas se os objetos dentro dela são mutáveis, é possível modificar os mesmos sem
#modificar a posição na memória da tupla
tupla=([1,2],[-1,-2])
id(tupla)
id(tupla[0])
tupla[0].append(3)
id(tupla)
id(tupla[0]) #modificamos a lista que fica na tupla, mas as posições na memória
#tanto da tupla quanto da lista que a integra continuam as mesmas

#quando fazemos um objeto igual a outro, o python faz referência à mesma posição
#na memória em ambos os casos
a=10
b=a
id(a)
id(b) #a e b fazem referência à mesma posição na memória
#no caso de dois objetos serem criados com o mesmo valor, o python automaticamente
#faz referência à mesma posição na memória ainsa que um objeto não
#tenha sido criado a partir do outro (MAS NEM SEMPRE, HÁ EXCESSÕES)
#isso só ocorre caso os valores dos objetos forem entre -5 e 256
c=4
d=4
id(c)
id(d) #c e d fazem referência à mesma posição na memória
e=400
f=400
id(e)
id(f) #c e d fazem referência posições distintas na memória

#podemos comparar duas variáveis quanto a serem ou não iguais por meio da posição
#na memória ou pelo conteúdo da variável
#o comando para verificar a posição na memória é is, is not para ver se é diferente
a is b
a is not b
#já o comando para comparar conteúdo é ==, != para ver se é diferente
a==b
a!=b
#CURIOSIDADE: None em python não é ausência de dado, mas um objeto
#dessa maneira, todos os objetos que forem iguais a None fazer referência à mesma
#posição na memória

#IMPORTANTE: ao aplicar for em um determinado objeto iterável, prefira criar
#este objeto como um conjunto (set), pois em comparação com as listas e as tuplas
#o código é lido muito mais rápido quando utilizamos conjuntos

#internamente, o python representa os números inteiros como liguagem binária,
#ou seja, nómeros na base 2

#o comando de divisão // nos fornece o valor inteiro de determinada divisão,
#já o comando % (conhecido como módulo) fornece o resto de uma divisão
#ATENÇÃO: essas características para // e % só são válidas para números positivos

#é possível representar números inteiros em diferentes bases, por exemplo, vamos
#representar 10 em binário e depois reverter o processo
x=bin(10)
y=int(x,base=2)

#podemos utilizar o método fraction para representar números racionais
#nesse método podemos passar qualquer número racional que ele será transformado
#em fração, podemos tanto escolher numerador e denominador como colocar qualquer
#número racional e a partir desse número é feita uma fração
from fractions import Fraction
meio=Fraction(1,2)
fracao=Fraction(3.141)
#todas as operações possíveis de serem aplicadas a números racionais também funcionam
#com o método Fraction
x=(Fraction(1,2)+Fraction(7,6))/Fraction(8,3)
#o python armazena os valores numéricos em números na base 2, por isso, valores
#como 0.1 que não tem uma representação exata na base dois, apresentam uma quantidade
#muito grande de algarismos plotado. Ao reverter os valores arquivados em base
#2 novamente para base 10, não temos um valor exato, mas um número decimal com
#uma grande quantidade de algarismos e que se aproxima de 0.1

#há vários métodos para arredondar números em python
#com trunc fazemos a truncagem, ou seja, apenas eliminamos a parcela decimal
#já com floor arredondamos como o menor valor inteiro mais próximo
#já ceil arredonda para o maior inteiro mais próximo
from math import trunc
from math import floor
from math import ceil
trunc(10.9),trunc(-10.9)
floor(10.9),floor(-10.9)
ceil(10.9),ceil(-10.9)

#por guardar números na base 2, o python nunca representa de maneira exata os decimais4
#dessa maneira, uma forma de representar este números é utilizando tuplas
#esses valores assumem o seguinte formato:
#(s, (d1, d2,....,dn), exp)
#em s representamo se o número é negativo ou positivo: 0 para positivo e 1 para negativo
#di representa cada um dos n algarismos do número
#exp representa o valor ao qual elevamos o 10 para representar o número
#por exemplo, o número -1,2345 é representado como:
n=(1,(1,2,3,4,5),-4)
import decimal
from decimal import Decimal
n2=Decimal(n)
#quando guardamos os númerosnessa forma de tuplas, temos seus valores precisos
#se guardarmos em forma decimal, o python vai guardar como um número na base 2
#que será apenas aproximadamente o que queremos representar na base 10
#é possível também representar estes valores como strings ao invés de tuplas

#a classe complex permite trabalhar com números imaginários em python
#a biblioteca math não funciona para números complexos, mas a cmath funciona
#os números complexos podem ser obtidos escrevendo z=x+yj ou complex(x,y)
z=5+4j
z.real,type(z.real)
z.imag,type(z.imag)
import cmath
#uma das utilidades da biblioteca cmath é converter coordenadas retangulares para polares
#o método phase nos dá o valor da reta
#já o método sbs nos informa o ângulo
cmath.phase(z) #ângulo
abs(z) #
#para ver o contrário, transformar cordenada polar em retengular, usar o método
cmath.rect(abs(z),cmath.phase(z))

#no caso de boleanos (TRUE or FALSE), o comando bool vai nos retornar FALSE para
#quaisquer valores diferentes de zero e TRUE para 0 ou NONE
#também irá retornar FALSE para objetos vazios como listas sem valores, dicionários, conjuntos, etc
u={}
l=[]
k=None
bool(1)
bool(u)
bool(l)
bool(k)
#são três os operadores em boleanos: not, and e or

#em funções, caso queiramos apresentar valores como padrão, temos que deixar os
#todos os valores pré-definidos por último, não podemos ter uma lista que conta
#com valores pré-definidos antes de algum que tenhamos que escolher
def area_retangulo(altura=0.1,largura=0.2):
    return 'A área do retângulo é {0} metros'.format(altura*largura)
#para especificar apenas um dos parâmetros aleatórios e deixar os outros com ovalor
#padrão, não importando se esse parâmetro pré definido é o primeiro ou o último
#devemos escrever os parâmetros que queremos associar a outros valores, deixando
#os demais em branco
area_retangulo(largura=0.00000001)
#o problema de nomear um argumento, e que não se pode colocar outros argumentos
#sem nomea-lo (ou nomeia, ou será utilizado o valor padrão)

#o que determina uma tupla não são os parênteses, mas as vírgulas entre os elementos
tupla1=(1,2,3)
tupla2=1,2,3
#é importante lembrar que dicionários e conjuntos são objetos não ordenados, de modo
#que estes não ficam em uma ordem específica, não sendo uma boa ideia iterar os mesmos
#para iterar, coloque os elementos dentro de uma tupla ou uma lista
#tudo que é iterável é possível de ser unphacked, da seguinte forma
string='abcde'
tupla=1,2,3,4,5
letra1, letra2, letra3, letra4, letra5=string
numero1, numero2, numero3, numero4, numero5=tupla
#agora é possível chamar cada elemento em separado, sem fazer referência ao conjunto
letra1
letra2
letra3
letra4
letra5
numero1
numero2
numero3
numero4
numero5
#já conjuntos e dicionários não são indexáveis, ou seja, você não tem como saber
#a ordem que eles vão aparecer caso sejam iteráveis
conjunto={1,2,3,4,'a','b','c','d'}
dicionário={'A': 'um','B':'dois','C':'três','D':'quatro','E':'cinco'}
c1,c2,c3,c4,c5,c6,c7,c8=conjunto
d1,d2,d3,d4,d5=dicionário
c1
c2
c3
c4
c5
c6
c7
c8
d1
d2
d3
d4
d5
#ao fazer o unpackeg de um dicionário, caso queiramos apenas seus valores e não
#os nomes que fazerm referência a eles, devemos utilizar o método .values
d1,d2,d3,d4,d5=dicionário.values()
d1
d2
d3
d4
d5
#com o método .items() temos tuplas
d1,d2,d3,d4,d5=dicionário.items()
d1
d2
d3
d4
d5
#nos casos de listas ou tuplas, podemos nos referir a termos específicos
#podemos utilizar também o comando * para que os termos restantes fiquem no 
#objeto de nosso interesse
l1=[1,2,3,4,'a','b','c','d']
l2=('um','dois','três','')
e1,e2,e3,e4,e5=l1[0],l1[1],l1[2],l1[3],l1[4:]
E1,*E2=l2
#uma maneira de extrair os elementos de uma tupla ou uma lista e utiliza-los
#individualmente é, na função, colocar um * antes do nome da lista
#para que toda a lista restante seja plotada devemos colocar *args
L=[1,2,3,'a','b','c',4,5,6,'d','e','f']
def func(x,y,z,*args):
    print(x)
    print(y)
    print(z)
    print(args)
func(*L)
#é possível colocar uma quantidade ilimitada de parâmetros em uma função
#especificando **kwargs na área de preenchimento da função
#todos os argumentos que especificamos se tornam key e values de um dicionário
def func2(**kwargs):
    print(kwargs)

#algumas vezes pode ser importante adcionar comentários às funções
def funcarg(x:'só vale valor numérico',
            y:'o valor padrão é 1, mas pode escolher outro se quiser'=1):
    '''Aqui vamos acrescentar alguns argumentos para você entender melhor
    o que essa função realmente faz'''
    return 'x*y é o equivalente a {0}'.format(x*y)
#devemos lembrar que expressões lambda são apenas para funções simples, de uma
#única linha de código
#para expressões mais complexas, deve-se utilizar def
#lambda não permite colocar comentários dentro da função
f=lambda x,*args,y,**kwargs:(x,*args,y,*kwargs) #importante, coloque sempre uma variável com valor determinado após *args, só assim sabemos quando vai acabar o quantidade de variáveis que vamos colocar
#a utilidade de uma função lambda é que ela pode ser expressa em uma única linha
#por isso, é possível alocar uma função lambda como um termo em outra função
def f2(fn,*args):
    return fn(args)
f2(lambda args: print(args),10,20,30,40)
#o comando sorted me permite ordenar os elementos de uma lista
#utilizando uma função lambda podemos estabelecer o critério de ordenação
#por exemplo, vamos ordenar um dicionário de acordo com seus valores, não keys
dic={'um':1,'dois':2,'três':3,'quatro':4,'cinco':5,'seis':6}
sorted(dic) #ordenação de acordo com os keys
sorted(dic,key=lambda e: dic[e]) #ordenação de acordo com os valores

#com compreensão em lista podemos aplicar uma determinada função individualmente
#a cada um dos elementos de uma lista
lista=[1,2,3,4]
lista2=[x**2 for x in lista]
#usando o comando zip, podemos agrupar em tuplas os termos das listas, podendo
#executar operações com estes termos por meio de compreensão em listas
lista3=[100,200,300,400]
lista4=[x+y for x,y in zip(lista,lista3)]
lista5=[x for x in lista if x%2==0]
lista6=[(x**2)-(y**4) for x,y in zip(lista3,lista) if (x**2)-(y**4)>10000]
#a função reduce vai permitir que possamos fazer uma iteração
#temos que fazer funções lambda comparando dois termos
#depois utilizamos reduce e conseguimos iterar de dois em dois termos de uma lista
#isso permite reduzir o nímero de linhas de código necessárias para se fazer
#um loop, compreensão em lista e função lambda nos permitem emular um loop
from functools import reduce
reduce(lambda x,y: x if x>y else y,lista)
#vamos agora fazer uma função mínimo
reduce(lambda x,y: x if x<y else y,lista)
#também é possível criar uma função fatorial
def fatorial(z): return reduce(lambda x,y: x*y if x*y>0 else 1,range(0,z+1))
#outra forma de fazer essas funções com ainda menos código que utilizando a função
#lambda é utilizando operadores
import operator
reduce(lambda x,y: x+y,lista)
reduce(operator.add(x,y),lista)

#o python tem variáveis de escopo global e local
#ao definir umavariável dentro de uma função, o python entende que o valor a ser
#utilizado para esta é o valor definido dentro da função
#se não há um valor estabelecido, deve utilizar valores globais, definidos fora de funções
#se também não há valores globais, procura-se as variáveis estabelecidas por padrão no python
var=10
def teste():
    a=10
    var=20 #a e var são locais, a função utiliza o valor local, o valor de antes não muda
    return 'a vale {0} e var vale {1}'.format(a,var)
teste()
var
#já se eu estabelecer dentro de uma função que vou utilizar o valor global de uma
#variável, posso modificar seu valor global dentro do ambiente da função, que é local
def teste2():
    a=10
    global var
    var=20 #a e var são locais, a função utiliza o valor local, o valor de antes não muda
    return 'a vale {0} e var vale {1}'.format(a,var)
teste2()
var

#devemos nos lembrar que quando utilizamos o @ para representar um decorador
#o que estamos fazendo é nada menos que colocandou ma função como parâmetro da
#função decoradora
from functools import wraps
def conter(fn):
    count=0
    @wraps(fn) #utilizando wraps(fn) toda a documentação e o nome da função que utilizamos como parâmetros é o que vão aparecer se chamamos o help após aplicar o decorador
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        print('{0} was called {1} times'.format(fn.__name__,count))
        return fn(*args,**kwargs) #a vantagem de usar esse número genérico é que de parâmetros é que poderemos aplicar esse decorador a funções com qualquer número de parâmetros
    return inner
#com base no código acima, o código logo abaixo permite contabilizar quantas vezes
#a função mult foi chamada no python, apenas utilizando @conter, sem precisar
#repetir o código acima colocando mult() como parâmetro
@conter
def mult(a,b,c=1):
    '''returns the product of three values'''
    return a*b*c
#outra forma de aplicar o mesmo decorador é:
mult=conter(mult)
#estabelecemos uma função como parâmetro de outra função
#quando utilizamos um decorador @, a função que vem logo em seguida passa a ser
#parâmetro daquela primeira que foi estabelecida e toda a vez que for chamada,
#teremos a função com decorador com insumo para a primeira

#vamos criar uma função que tem outra função como parâmetro e busca calcular quantas vezes a função utilizada como parâmetro foi invocada
from functools import wraps
def counter(fn):
    count=0
    def inner(*args,**kwargs):
        '''this is the inner clousure'''
        nonlocal count
        count+=1
        print('Function {0} (id={1} was called {2} times)'.format(fn.__name__,id(fn),count))
        return fn(*args,**kwargs) #como não sabemmos quantos parâmetros tem a função fn, temos que colocar o número de parâmetros da maneira mais genérica possível
    inner=wraps(fn)(inner) #essa linha é para que o help da função fn após for decorada, chame os dados da função fn, não do decorador
    return inner
def mult(a:int,b:int,c:int,d):
    '''Function that multiplies values'''
    return a*b*c*d
help(mult)
#agora vamos decorar e ver se mantem o help
@counter
def mult(a:int,b:int,c:int,d):
    '''Function that multiplies values'''
    return a*b*c*d
help(mult)

#vamos fazer mais algumas funções com decoradores
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    @wraps(fn)
    def inner(*args,**kwargs):
        run_dt=datetime.now(timezone.utc)
        result=fn(*args,**kwargs)
        print('{0}: called {1}'.format(run_dt,fn.__name__))
        return result
    return inner

def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start=perf_counter()
        result=fn(*args,**kwargs)
        end=perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__,end-start))
        return result
    return inner

#vamos fazer uma função que nos fornece
@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce
    return reduce(mul,range(1,n+1))

def fact(n):
    from operator import mul
    from functools import reduce
    return reduce(mul,range(1,n+1))

fact=logged(timed(fact))

#é possível fazer um decorador utilizando classes ao invés de funções
class MyClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __call__(self,fn):
        def inner(*args,**kwargs):
            print("decorated function calle: a={0}, b={1}".format(self.a,self.b))
            return fn(*args,**kwargs)
        return inner
def my_func(s):
    print("Hello {0}".format(s))
#agora vamos decorar
@MyClass(10,20)
def my_func(s):
    print("Hello {0}".format(s))

#suponhamos que temos uma classe, é possível utilizar o mesmo método de decoradores
#para acrescentar um determinado método a uma classe
def dec_speak(cls): #veja que o insumo é uma classe, não uma variável
    cls.speak=lambda self, message: '{0} says: {1}'.format(self.__class__.__name__, message)
    return cls
from fractions import Fraction
Fraction=dec_speak(Fraction) #pronto, já acrescentei este método
f1=Fraction(2,3)
f1.speak('hello')
class Person:
    pass
Person=dec_speak(Person)
p=Person()
p.speak('this works!')


#agora o assunto são tuplas
#o que é importante é que as tuplas são imutáveis, não é possível acrescentar ou retirar elementos da tupla
#mas se os elementos da tupla são mutáveis, é possível modificar os mesmos sem que a tupla se modifique
#a posição na memória a qual um elemento da tupla faz referência é imutável
#vamosfazer uma lista com tuplas que nos dão idade, ano de nascimento e nº de filhos de
#cada pessoa, respectivamente nas posições 0,1 e 2 de cada tupla desta lista
lista=[(15,2005,0),(30,1990,2),(45,1975,5)]
#vamos somar o total defilhos desse grupo que faz parte desta lista
filhos=0
for x in lista:
    filhos+=x[2]
    print('{0} filhos no total'.format(filhos))
#caso tenhamos uma tupla e queiramos selecionar apenas alguns elemento tupla
#seja como objetos ou novas tuplas, devemos utilizar *_ para representar aqueles
#elementos que nós não queremos
tupla1=10,"cavalo",[1,2,3],0.15 #lembrando que não precisamos de parênteses para definir uma tupla, apenas as vírgulas são suficientes
#quero só 10 e 0.15
dez,*_,zerovirgulaquinze=tupla1
#agora eu não quero cavalo
numero,*_,listinha,valor=tupla1
#podemos usar namedtuples, pois assim fica mais fácil chamar os elementos de uma tupla
from collections import namedtuple
tupla3d=namedtuple('tupla3d', ['x','y','z']) #primeiro passamos o nome da classe e depois os nomes dos campos
tresvalores=tupla3d(1,2,3)
tresvalores
tresvalores.x
tresvalores.y
tresvalores.z
#como não é possível mudar o valor de um objeto em uma tupla, é necessário criar outra
#tupla com novos valores
t2d=namedtuple('tupla2d',['v1','v2'])
novatupla=t2d(1,2)
novatupla
#supondo que eu queira mudar só o valor v1
novatupla=t2d(3,novatupla.v2)

#agora vou fazer uma tupla nomeada (named tuple)
from collections import namedtuple
Point2D=namedtuple("Point2D","x1 y1 x2 y2 xorigem yorigem")
#agora vou estabelecer valores padrão
v1=Point2D(0,0,0,0,0,0)

#agora vamos estudar módulos
#os módulos são nada mais que instâncias do tipo módulo
#importamos bibliotecas e módulos
#quando utilizamos os códigos from X import Y, o x se refere à biblioteca e o y se refere ao módulo
#o que utilizamos com . é o método, exemplo, .name, .área (nas classes que eu criei para medir área) são métodos não módulos

#já os pacotes podem conter outros pacotes ou módulos
#quando estraimos um módulo que está dentro de um pacote, escrevemos primeiro
#o nome do pacote e depois do módulo, separados por um ponto
#ex: from biblioteca import pacote.módulo

#aqui veremos alguns comandos para objetos sequenciais
lista=["a","b","c","d",100,200,300,400]
#podemos modificar o elemento de índice i de uma lista por x apenas fazendo: lista[i]=x
lista[0]="A"
#podemos também deletar um elemento
del lista[3:5]
#com append acrescentamos uma elemento ao fim go iterável e com insert, acrescentamos
#x na posição i
lista.append(500)
lista.insert(3,"d")
lista.insert(4,100)

#quando colocamos apenas igual para fazer uma cópia de um objeto criamos um novo objeto
#que faz referência à posição da memória do objeto inicial de modo que, se modificarmos
#o objeto inicial a cópia também é modificada. Para evitar isso, podemos copiar um objeto
#fazendo um deepcopy
from copy import copy, deepcopy
lista1=[1,2,3,4,5]
lista2=deepcopy(lista1)
lista3=lista1
lista1[1] is lista2[1]
lista1[1] is lista3[1]
l=lista1.copy()

#podemos fatiar um objeto iterávvel selecionando o intervalo que queremos
#considerar dentro deste ojeto e selecionando se vamos querer todos ou apenas alguns
#termos selecionados de acordo com nossa necessidade
z=lista1[1:5] #estou selecionando os termos dos índices de 1 a 4, pois o extremo direito do intervalo não é considerado
z1=lista1[1:5:1] #basicamente fizemos o mesmo
z2=lista2[1:5:2] #vamos pegar um em cado dois termo do índice 1 ao 4, começando do 1

#para fazer o comando concatenar, basta utilizar o comando +
lista1=[1,2,3]
lista2=[3,4,5]
lista3=lista1+lista2
tupla1=1,2,3
tupla2=3,4,5
tupla3=tupla1+tupla2

#já para fazer com que os valores de um iterável se repitam, devemos utilizar *
l1=[0,1,2,3,4]
l2=l1*2
t1=0,1,2,3
t2=t1*3

#é possível acrescentar e eliminar elementos de um objeto iterável, como vamos mostrar agora
l1=[10,20,30,40,50,60]
#vamos eliminar
l1[0:3]=[]
#vamos acrescentar
l1[0:0]=[10,20,30]

#o comando sorted me permite ordenar parâmetros de um objeto de maneira crescente
#como padrão e decrescente quando quisermos
lista1=[5,10,15,20,25,30]
sorted(lista1,reverse=True)
#no caso de dicionários, ao chamar o índex, fazemos referência aos valores e não as
#keys, e é assim que fazemos a ordenação com base nos keys
dic1={"A":100,"B":10,"C":1}
sorted(dic1,key=lambda x: dic1[x])
#a função sorted sempre nos dá como resposta uma lista, mesmo quando queremos ordenar
#uma tupla, por exemplo, vamos ordenar uma tupla de acordo com o tamanho dos termos
t="uva","cavalo","Divinópolis"
sorted(t,key=lambda x: len(x))
#agora do maior para o menor
sorted(t,key=lambda x: len(x),reverse=True)
#obviamente que o mesmo vale para lista, sendoque podemos emular a opção reverse=True
#colocando o negativo na frente de len()
list="essa frase tem que ser dividida em palavras".split()
sorted(list,key=lambda x:-len(x))
#em list compreention a ordem édistinta, a órdem é:trnasformation, iteration, filter
#em um loop a órdem é: iteration, filter, transformation
lista=[0,1,2,3,4,5,6,7,8,9,10]
#loop
nova_lista=[]
for x in lista:
    if x>5:
        nova_lista.append(x)
#agora vamos fazer a mesma função em compreensão em lista
new_list2=[x for x in lista if x>5]
l=[]
for i in range(1,10):
    if i%2==0:
        for j in range(1,10):
            if j%3==0:
                l.append((i,j))
#agora list comprehension
[(i,j) for i in range(1,10) if i%2==0 for j in range(1,10) if j%3==0]

import math
class poligon:
    def __init__(self,edges,circumradius):
        self.n=edges
        self.R=circumradius
        self.interior_angle=(self.n-2)*(180/self.n)
        self.edge_length=2*self.R*math.sin(math.pi/self.n)
        self.apothem=self.R*math.cos(math.pi/self.n)
        self.area=0.5*self.n*self.apothem*self.edge_length
        self.perimeter=self.n*self.edge_length
    def __len__(self):
        return self.n
    def __repr__(self):
        return 'Polinômio com {0} arestas, círculo {1}, àngulo interior {2}, aresta de tamanho {3}, apótema {4}, área {5} e perímetro {6}'.format(self.n,self.R,self.interior_angle,self.edge_length,self.apothem,self.area,self.perimeter)
    def __eq__(self,other_edges,other_circumradius):
        if isinstance(other_edges,poligon) and isinstance(other_circumradius,poligon):
            return self.edges==other_edges.n and self.circumradius==other_circumradius.R
        else: False
    def __gt__(self,other_edges):
        if isinstance(other_edges,poligon):
            return self.edges>other_edges.n
        else: False

class Polygon:
    def __init__(self,n,R):
        self._n=n
        self._R=R
    def __repr__(self):
        return 'Polygon(n={0}, R={1}}'.format(self._n,self._R)
    @property
    def count_vertices(self):
        return self._n
    @property
    def count_edges(self):
        return self._n
    @property
    def circumradius(self):
        return self._R
    @property
    def interior_angle(self):
        return(self._n-2)*180/self.n
    @property
    def side_length(self):
        return 2*self._R*math.sin(math.pi/self._n)
    @property
    def apothem(self):
        return self._R*math.cos(math.pi/self._n)
    @property
    def area(self):
        return self._n/2*self.side_length*self.apothem
    @property
    def perimeter(self):
        return self._n*self.side_length
    def __eq__(self,other):
        if isinstance(other,self.__class__):
            return (self.count_edges==other.count_edges and self.circumradius==other.circumradius)
        else:
            return NotImplemented
    def __gt__(self,other):
        if isinstance(other,self.__class__):
            return self.count_vertices>other.count_vertices
        else:
            return NotImplemented
    def __it__(self,other):
        if isinstance(other,self.__class__):
            return self.count_vertices<other.count_vertices
    def __le__(self,other):
        if isinstance(other,self.__class__):
            return self.count_vertices<=other.count_vertices
    def __ne__(self,other):
        if isinstance(other,self.__class__):
            return self.count_vertices!=other.count_vertices
    def __ge__(self,other):
        if isinstance(other,self.__class__):
            return self.count_vertices>=other.count_vertices

#vamos criar iteradores, sem a necessidade do comando for
class Squares:
    def __init__(self,length):
        self.length=length
        self.i=0
        
    def __next__(self):
        if self.i>=self.length:
            raise StopIteration
        else:
            result=self.i**2
            self.i+=1
            return result
#acrescentando __iter__ podemos iterar nosso objeto criado
class Squares:
    def __init__(self,length):
        self.length=length
        self.i=0
        
    def __next__(self):
        if self.i>=self.length:
            raise StopIteration
        else:
            result=self.i**2
            self.i+=1
            return result
        
    def __iter__(self):
        return self

#vejamos mais esse exemplo de como fazer um iterador
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

#IMPORTANTE: o mais importante disso tudo é lembrar da diferença entre iteradores e iteráveis
#iteradores são objetos que se esgotam após serem iterados, por exemplo os objetos das classes que criamos acima, como PowTwo
#iteráveis são objetos que podem ser iterados várias vezes, como listas, tuplas e dicionários

#caso haja dúvida, basta verificar se a classe a qual pertence o objeto tem o método __next__, se tiver é iterador, pois o iterável só tem __iter__, ao passo que o iterador tem os dois

#para fazer objetos iteráveis, devemos adcionar às classes o método __getitem__
#ver exemplo abaixo
class Squares:
    def __init__(self,n):
        self._n=n
    def __len__(self):
        return self._n
    def __getitem__(self,i):
        if i>=self._n:
            raise IndexError
        else:
            return i**2
for i in A:
    print(i) #como vê, é possível repetir indefinidamente
             #a utilização do método __getitem__ reduz a necessidade de código em comparação a utilização de outras funções

#existe uma maneira muito mais simples de criar iteradores, que consiste na utilização de geradores
#geradores são funções com o comando yield, que apresentam as mesmas propriedades dos iteradores
#a diferença é que o número de linhas de código necessárias para elaborar um gerador é muito menor que para um iterador
#vamos criar dois iteradores fatorial, com sem o uso de geradores e outro com um gerador
import math
class FactIter:
    def __init__(self,n):
        self.n=n
        self.i=0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.i>=self.n:
            raise StopIteration
        else:
            result=math.factorial(self.i)
            self.i+=1
            return result

fact_iter=FactIter(5)

def fact():
    i=0
    def inner():
        nonlocal i
        result=math.factorial(i)
        i+=1
        return result
f=fact()
f()
f()
f()
f()
f()

def my_func():
    print('line 1')
    yield 'Flying'
    print('line 2')
    yield 'Circus'

f=my_func()
next(f)
next(f)

def silly():
    yield 'the'
    yield 'ministry'
    yield 'of'
    yield 'silly'
    if True:
        return 'Sorry, all done!"
    yield 'walks'
gen=silly()
for line in gen:
    print(line)

import math
def fact(n):
    for i in range(n):
        yield math.factorial(i)

gen=fact(5)

def squares(n):
    for i in range(n):
        yield i**2

sq=squares(5)
list(sq)

#a vantagem de criar iteradores por meio de geradores é que gastamos bem menos espaço na memória
#mas podemos também criar objetos iteráveis utilizando geradores, que quer dizer que eles não se esgotam quando utilizamos uma única vez
def squares(n):
    for i in range(n):
        yield i**2

class Squares:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return squares(n)
sq1=Squares(5)
l1=list(sq1)
sq2=Squares(3)

#é possível aplicar a mesma sintaxe de compreensão em listas para criar iteradores ao invés de iteraveis
#substituindo os colchetes por parênteses, os geradores possibilitarão criar iteradores, ou seja, funções que se esgotam após aplicadas uma vez
x=[i**2 for i in range(5)]
y=(i**2 for i in range(5))
list(x)
list(x) #iterável, posso repetir o quanto quiser
list(y)
list(y) #iterador, só posso utilizar uma vez

#agregadores são funções que tem como insumo ojetos ideráveis e que retornam um único valor
#vamos usar boleanos, então é bom saber que ao aplicar boleanos em uma lista de objetos, teremos que
#um boleano nos dá resultado false nos casos de:0,false,objeto vazio (listas vazias, tuplas vazias, etc)
#Atenção: isso vale no caso de iterárqmos, considerando a lista como um todo, sempre que elas está não vazia nos dará resultado true, mesmo se o objeto for zero
#as funções any e all analisam cada elemento de um iterável. any retorna false se algum elemento da lista é falso. all retorna false se todos os elementos do objeto são falsos.
any([0,'',None]) #se algum for verdadeiro, vai retornar true
all([0,'',None]) #se todos os objetos forem verdadeiro
any([0,'',None,(10,20)]) #se algum for verdadeiro, retorno verdadeiro
all([0,'',None,(10,20)])

#a função map permite aplicar uma função específica a todos os objetos de um outro objeto iterável
#vamos testar abaixo se todos os termos da lista l são números
l=[0,1,2,3,4,"cavalo"]
all(map(lambda x: isinstance(x, Number),l))

#a função islice permite que façamos segmentação mesmo de objetos não iteráveis
import math
from itertools import islice
def slice_(iterable, start, stop):
    for _ in range(0, start):
        next(iterable)
    for _ in range(start,stop):
        yield next(iterable)
list(islice(factorials(100),3,10))

#as funções getcontext() permitem modificar algumas configurações do python
#com elas é possível modificar a configuração que se quer, executar o código nesse novo contexto e encerra-lo, fazendo com que as configurações voltem ao padrão
#nesse caso, a manipulação vale apenas para o código que está entre a mudança de configuração e o retorno à configuração inicial
#tudo o que for escrito depois ou antes é feito dentro das configuração padrão
#exemplo, mudança de casas decimais exibidas
x=0.999999
x
import decimal
old_prec=decimal.getcontext().prec
decimal.getcontext().prec=5
x
decimal.getcontext().prec=old_prec

#Há duas maneiras de fazer um dicionário, podemos faze-lo abrindo as chaves e estabelecendo keys e values
d1={i:i**2 for i in range(1,5)} #usando compreensão em dicionários
d2={}
for i in range(1,5):
    d2[i]=i**2 #não usando compreensão em dicionários
#a outra maneira é como mostrado abaixo
#com o método from keys é possível criar dicionários
#mas nesse caso, todas as keys tem que apresentar o mesmo valor
d3=dict.fromkeys(["um","dois","três","quatro","cinco"],7)

#vamos falar um pouco sobre conjuntos
s1={"a","b","c","d"} #conjunto 1
s2={"b","c","d","e"} #conjunto 2
s1 | s2 #união dos dois conjuntos
s1 & s2 #intersessão dos dois conjuntos

#agora vamos estudar conjuntos
s1={1,2,3}
s2={3,4,5}
s1|s2
s1^s2
s1-s2
s1&s2
#importante: no caso de conjuntos, para criar um conjunto vazio devemos usar set()
#o comando {} cria um dicionário vazio

#no caso de atributos em classes nós utilizamos ponto, ".", seguido do atributo
#no caso de funções (métodos), devemos utilizar o ponto com a função seguida de parênteses
