# Aula 01:
print('Meu primeiro programa em Python')
a = 2
b = 3
soma = a + b
print(soma)


# Aula 02: Variáveis e operadores
a = 10
b = 6
a = int(input('Entre com o primeiro valor: ')) #input armazena string
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma)) #type int
soma = str(soma) #converte em string
print(type(soma)) #type string
print('soma: ' + soma)
print('subtracao: ' + str(subtracao))
print('multiplicacao: {}'.format(multiplicacao)) #concatena tipos diferentes em string
print(divisao)
print(type(divisao)) #type float
print(int(divisao)) #type int
print(resto)

print('Soma: {}. Subtracao: {}.'.format(soma, subtracao))
resultado = ('Soma: {soma}. \nSubtração: {sub}.'
      '\nMultiplicação: {mult}'
      '\nDivisão: {div}'
      '\nResto: {resto}'.format(soma=soma,
                                sub=subtracao,
                                mult = multiplicacao,
                                div = divisao,
                                resto = resto))

print(resultado)
print(type(resultado))
x = '1'
soma2 = int(x) + 1
print(soma2)


# Aula 03: 
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))
print('Final do programa')

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or not resto_b == 1:
    print('Foi digitado um número par')
else:
    print('Nenhum número par foi digitado')

a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
print('media: {}'.format(media))


# Aula 04: if, for, while
a = int(input('Entre com um número: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div += 1

if div == 2:
    print('número {} é primo'.format(a))
else:
    print('número {} não é primo'.format(a))

a = int(input('Entre com um valor: '))
for num in range(1,a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1

    if div == 2:
        print(num)

a = 0
while a <= 10:
    print(a)
    a += 1


# Aula 05: lista e tupla
lista = [1, 3, 5, 7]
lista_animal = ['cachorro','gato','elefante']
print(lista)
print(type(lista)) #type list
print(lista_animal[1])

for x in lista_animal:
    print(x)

print(sum(lista))
print(min(lista))
print(max(lista))
print(min(lista_animal)) #Ordem alfabética primeira letra
print(max(lista_animal))

nova_lista = lista_animal * 3
print(nova_lista)

if 'gato' in lista_animal:
    print('existe um gato na lista')
else:
    print('não existe um gato na lista')

if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('não existe um lobo na lista')
    lista_animal.append('lobo')
    print(lista_animal)

lista_animal.pop() #Retira último da lista
print(lista_animal)

lista_animal.pop(0) #Retira um elemento pelo índice
print(lista_animal)

lista_animal.remove('elefante') #Retira um elemento da lista
print(lista_animal)


lista = [12, 10, 7, 5]
lista_animal = ['cachorro','gato','elefante','lobo','arara']

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)


lista = [12, 10, 7, 5]
lista_animal = ['cachorro','gato','elefante','lobo','arara']
lista_animal[0] = 'macaco' #lista é mutável

tupla = (1, 10, 12, 14) #tupla é imutável
print(tupla)
print(tupla[0])
print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)


# Aula 06: conjuntos (set)
conjunto = {1, 2, 3, 4}
print(type(conjunto)) #type: set, não pode repetir elementos
conjunto.add(5)
conjunto.discard(2)
print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_intersercao = conjunto.intersection(conjunto2)
print('Interseção: {}'.format(conjunto_intersercao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
print('Diferença 1 e 2: {}'.format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('subset: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('superset: {}'.format(conjunto_superset))

lista = ['cachorro','cachorro','gato','gato','elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)


# Aula 07: classes, métodos e funções
class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    # função
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

calculadora = Calculadora(10, 2)
print(calculadora.a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())


class Calculadora2:
    def __init__(self):
        pass

    # função
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

calculadora = Calculadora2()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicacao(10, 5))
print(calculadora.divisao(100, 2))


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    # Método, sem return
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

televisao = Televisao()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))

print('Canal: {}'.format(televisao.canal))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))


# Aula 08: módulos, métodos, funções lambda
Python console:
import modulo
from modulo import classe

def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

def teste():
    return ('teste')

if __name__ == '__main__':
    lista = ['cachorro','gato']
    print(contador_letras(lista))


from aula07_televisao import Televisao
from aula07_calculadora1 import Calculadora
from aula08_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro','gato','elefante']
    print(contador_letras(lista))
    print(teste())


contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro','gato','elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda  a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora)) #type dictionary
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print(soma(10, 5))
print(multiplicacao(10, 2))


# Aula 09: Arquivos externos
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/Silas/PycharmProjects/pythonProject/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        print(lista_notas)
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Silas/PycharmProjects/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Silas/PycharmProjects/')


if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)


# Aula 10: data
from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(type(horario))
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))
    print(horario_str)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.date())
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)

    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()


# Aula 11: Exceções com try, except, else e finally
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    # x = a

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()


class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)


# Aula 12: Pacotes e requests
Terminal:
pip install requests

