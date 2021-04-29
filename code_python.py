# -*- coding: utf-8 -*-
# Comentário ativo para permitir os acentos

""" Arquivos python usam extensão .py
Linguagem case sensitive
Não usa ; e não precisa declarar tipo da variável
Python usa TAB para separar blocos
Usa \n para quebra de linha
POO: objeto.atributo e objeto.método()
# Para um comentário. Três aspas para bloco de comentários."""

""" Operadores:
+  soma
-  subtração
*  produto
/  divisão
%  módulo
** exponenciação
x+=1 contador"""

""" Operadores relacionais:
== igual a
!= diferente de
>  maior que
<  menor que
>= maior ou igual a
<= menor ou igual a"""

"""Operadores lógicos:
AND e
OR  ou
NOT não"""

# if CONDIÇÃO:
#		AÇÃO
# elif CONDIÇÃO:
#		AÇÃO
# else:
#		AÇÃO
x = 1
y = 2
if x>y:
	print("x maior")
elif x==y:
	print("x igual a y")
else:
	print("y maior")

# while CONDIÇÃO:
#		AÇÃO
while x<3:
	print(x)
	x += 1

# for
vetor = [1,3,5]
for i in range(0,5): # for i vai valer 0, 1, 2, 3, 4
	print(i)
for i in vetor: # for i vai valer cada valor do vetor
	print(i)
for i in range(10): # i de 0 até 9
	print(i)
for i in range(10,20,2): # i começa de 10 a 18, de 2 em 2
	print(i)

# Strings
a = "A"
b = "Ba"
c = a + " " + b # concatenando strings
tamanho = len(c) # função retorna length do vetor
# vetor[] índice específico
# vetor[0:4] sequência
# vetor[0:] até o final
c = c.lower() # todos minúsculos
c = c.upper() # todos maiúsculos
c = c.strip() # remove espaço e caracter especial como \n no início e fim
d = c.split() # converte string em lista. O padrão é por espaços
d = c.split("char") # converte em lista separando por char
e = c.find("termo") # retornar o índice do substring
c = c.replace("termo","substituto") # substitui o termo por substituto

# Funções
# def NOME(PARÂMETROS):
#		COMANDOS
# Chamanda:
# NOME (ARGUMENTOS)
def soma(x,y):
	return(x+y)

# Arquivos
# variavel = open(nome,modo)
# Modo:
# r  somente leitura
# w  escrita (apaga e recria)
# a  leitura e escrita (no fim do arquivo)
# r+ leitura e escrita
# w+ escrita (apaga e recria)
# a+ leitura e escrita (abre arquivo para atualização)

# read(): Lê arquivo inteiro
# readline(): Lê uma linha
# readlines(): Lê arquivo e o armazena em uma lista
# write("texto"): Escreve
# close(): Fecha
arquivo = open("arquivo.txt")
texto = arquivo.read()
print(texto)
arquivo.close()

w = open("arquivo2.txt","w")
w.write("Esse eh meu arquivo\n")
w.close()

# Vetores
# Adicionar valores
# vetor.append("valor")
vetor.append(7)
# Checa presença no vetor
# if Valor in vetor:
if 7 in vetor:
	print("7 está no vetor")
# Remover elemento
# del vetor[x:y]
del vetor[2:]
# Ordenar o vetor
vetor.sort() # Altera a lista original
vetor = sorted(vetor) # função que retorna vetor ordenado
# Ordenar decrescente
vetor.sort(reverse=True)
# Inverter o vetor
vetor.reverse()

# Dicionários
# dicionario = {"chave":"valor"}
lista = {"A":"AMEIXA","B":"BOLA","C":"CASA"}
print(lista["A"]) # Imprime AMEIXA
for chave in lista:
	print(lista[chave]) # imprime: AMEIXA BOLA CASA
for i in lista.items():
	print(i) # imprime os itens
for i in lista.values():
	print(i) # imprime os valores: AMEIXA BOLA CASA
for i in lista.keys():
	print(i) # imprime as chaves: A B C

import random # Biblioteca random
# Ex: Instalação biblioteca pandas
# Anaconda Powershell Prompt: pip install pandas

# var = random.randint(x,y)
# Cria um número random entre x e y
random.seed(1) # força a fixar em um número
numero = random.randint(0,10)
# var = random.choice(vetor)
# Escolhe um do vetor
numero = random.choice(vetor)

# Tratamento de exceções
# try:
#		AÇÃO
# except:
#		AÇÃO
# Age em casos de erro no try como divisão por zero

# Input
string = input("Digite um texto: ")
numero_inteiro = int(input("Digite um numero inteiro: "))
numero_decimal = float(input("Digite um numero decimal: "))

# Raiz quadrada
from math import sqrt

# list comprehension
x = [1, 2, 3, 4, 5]
y = []
# modo tradicional de fazer x ao quadrado
for i in x:
	y.append(i**2)
# usando list comprehension
# y = [valor_a_adicionar laço condição]
y = [i**2 for i in x] # retorna x ao quadrado
z = [i for i in x if i%2==1] # retorna ímpares

# Função enumerate
# modo tradicional para achar os índices
for i in range(len(vetor)):
	print(i,vetor[i])
# usando enumerate
for i, nome in enumerate(vetor):
	print(i,nome)

# Função map: aplica função em vetor
# map(função,vetor)
def dobro(x):
	return x*2
mapa = map(dobro,vetor)
print(list(mapa)) # torna tipo map em lista

# Função reduce
# Recebe um vetor e retorna a soma de seus valores
# reduce(função,vetor)
from functools import reduce
def soma(x,y):
	return x+y
soma = reduce(soma,vetor)

# Função zip
# Concatena 2 ou mais vetores índice a índice
v1 = [1, 2, 3, 4, 5]
v2 = ["ARROZ","BOLA","CASA","DADO","ELEFANTE"]

for numero,nome in zip(v1,v2):
	print(numero,nome)