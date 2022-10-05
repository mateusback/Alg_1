#1
# definindo o vetor
v = [0] * 100

# inserindo valores no vetor
for i in range(1, len(v)+1):
    v[i-1] = i

# a
for i in range(0, len(v)):
    print(v[i])

# b
for i in range(len(v)-1, -1, -1):
    print(v[i])

# c
for i in range(0, len(v)):
    print("O dobro de", v[i], "é:", v[i]*2)

# d
soma = 0
for i in range(0, len(v)):
    soma += v[i]
print("A soma de todos os números é:", soma)

# e
soma = 0
media = 0
for i in range(0, len(v)):
    soma += v[i]
media = soma / len(v)
print("A média geral entre os valores é:", media)

# f
for i in range(0,len(v)):
    if (v[i] % 2 == 0):
        print(v[i])

#2
import random
v = [0] * 6
vsorte = [0] * 6

for i in range(0, len(v)):
    v[i] = int(input(f"Informe o {i+1}° valor: "))
    vsorte[i] = random.randint(1, 100)
for i in range(0, len(vsorte)):
    print(f"O {i+1}° número sorteado foi:", vsorte[i])

#3
v = [''] * 5

for i in range(0, len(v)):
    v[i] = input(f"Informe o nome do {i+1}° aluno: ")

for i in range(0, len(v)):
    print(f"O nome do {i+1}° aluno é:", v[i])

#4
v = [0] * int(input("Informe o tamanho do vetor: "))

for i in range(0, len(v)):
    v[i] = int(input(f"Informe o {i+1}° valor: "))

for i in range(0, len(v)):
    print(f"Informe o {i+1}° valor digitado foi:", v[i])

#5
from xmlrpc.client import MAXINT, MININT

# definindo o vetor:
v = [0] * int(input("Informe o tamanho do vetor: "))

# informando os valores do vetor:
for i in range(0, len(v)):
    v[i] = int(input(f"Informe o {i+1}° valor: "))

# a
for i in range(len(v)-1, -1, -1):
    print(f"Informe o {i+1}° valor digitado foi:", v[i])

# b
soma = 0
for i in range(0, len(v)):
    soma += v[i]
print(f"A soma dos {len(v)} valores infomados é:", soma)

# c
soma = 0
media = 0
for i in range(0, len(v)):
    soma += v[i]
media = soma / len(v)
print(f"A média geral dos {len(v)} valores informados é:", media)

# d
for i in range(0, len(v), 2):
    print(f"O valor {v[i]} está em um índice de número par ({i})")

# e
alpha = int(input("Informe o índice inicial de busca: "))
omega = int(input("Informe o índice final de busca: "))

for i in range(alpha, omega+1):
    print(v[i])

# f
alpha = int(input("Informe o índice inicial de busca: "))
omega = int(input("Informe o índice final de busca: "))
soma = 0

for i in range(alpha, omega+1):
    soma += v[i]
print(f"A soma dos valores entre os índices {alpha} e {omega} é:", soma)

# g
maior = MININT
menor = MAXINT
for i in range(0, len(v)):
    if (v[i] >= maior):
        maior = v[i]
    elif (v[i] <= menor):
        menor = v[~i]
print(f"{maior} foi o maior valor iformado")
print(f"{menor} foi o maior valor iformado")

# h
maior = MININT
menor = MAXINT
pmaior = 0
pmenor = 0
for i in range(0, len(v)):
    if (v[i] >= maior):
        maior = v[i]
        pmaior = i
    elif (v[i] <= menor):
        menor = v[~i]
        pmenor = i
print(f"{menor} foi o menor valor iformado e está no índice {pmenor}")
print(f"{maior} foi o maior valor iformado e está no índice {pmaior}")
    
# i
par = 0
impar = 0
for i in range(0, len(v)):
    if (v[i] % 2 == 0):
        par += 1
    else:
        impar += 1
print(f"A quantidade de números pares informados foi de: {par}")
print(f"A quantidade de números impares informados foi de: {impar}")

#6 - null

#7
vAlunos = [''] * int(input("Informe o número de alunos: "))
vConceitos = [''] * len(vAlunos)

for i in range (0, len(vAlunos)):
    vAlunos[i] = input(f"Digite o nome do {i+1}° aluno: ")
    vConceitos[i] = input(f"Informe o conceito do(a) {vAlunos[i]}: ")

for i in range (0, len(vAlunos)):
    print(f"{vAlunos[i]} ficou com o conceito: {vConceitos[i]}")

#8
vSorteados = [0] * 6
vApostados = [0] * 6
acertos = 0

for i in range(0, len(vSorteados)):
    vSorteados[i] = int(input(f"Informe o {i+1}° valor sorteado: "))
print("-------------")
for i in range(0, len(vApostados)):
    vApostados[i] = int(input(f"Informe o {i+1}° valor apostado: "))
    if (vApostados[i] == vSorteados[i]):
        acertos += 1
if (acertos <= 3):
    print(f"Você acertou {acertos}, e não ganhou nada")
elif (acertos == 4):
    print("Você acertou a quadra!")
elif (acertos == 5):
    print("Você acertou a quina!")
else:
    print("Você nunca mais vai precisar trabalhar!")

#9
import random

v = [0] * 6
sorteados = random.sample(range(1, 100), 6) #gerando uma amostra entre 1 e 100 de 6 números
acertos = 0

for i in range (0, len(sorteados)):
    print(sorteados[i])
for i in range(0, len(sorteados)):
    v[i] = int(input(f"Informe o {i+1}° valor apostado: "))

# bouble
for i in range(len(sorteados)-1, 0, -1):
    for j in range (0, i):
        if sorteados[j]>sorteados[j+1]:
            aux = sorteados[j+1]
            sorteados[j+1] = sorteados[j]
            sorteados[j]= aux

for i in range (0,len(v)):
    if (v[i] == sorteados[i]):
        acertos +=1
if (acertos <= 3):
    print(f"Você acertou {acertos}, e não ganhou nada")
elif (acertos == 4):
    print("Você acertou a quadra!")
elif (acertos == 5):
    print("Você acertou a quina!")
else:
    print("Você nunca mais vai precisar trabalhar!")

#10
nome = input("Digite um nome: ")
v = list(nome)
primeira = 0
ultima = len(v)-1
while (primeira <= ultima):
    aux = v[primeira]
    v[primeira] = v[ultima]
    v[ultima] = aux
    primeira +=1
    ultima -= 1
print(v)

#11
import random
pessoas = [''] * 10
for i in range (0,len(pessoas)):
    pessoas[i] = input(f"Informe o nome da {i+1}° pessoa: ")
print(f"A pessoa escolhida foi: {pessoas[random.randint(0,10)]}")

# 12
pergunta = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
resposta = [''] * len(pergunta)
cont = 0
for i in range (0,len(pergunta)):
    print(pergunta[i])
    resposta[i] =  str.lower(input("S/N: "))
    if (resposta[i] == "s" or resposta[i] == "sim"):
        cont += 1
print("-------------")
if (cont == 2):
    print ("Suspeita")
elif (cont>=3 and cont<=4):
    print ("Cúmplice")
elif(cont==5):
    print("Assassino")
else:
    print("Inocente")

# 13
cont = 0
votos = [1]
deusMeAjude = 0
sistema = [0] * 6
while (votos[cont] != 0):
    deusMeAjude = int(input(
        f"Qual o melhor Sistema Operacional para uso em servidores?\n 1- Windows Server \n 2- Unix\n 3- Linux\n 4- Netware\n 5- Mac OS\n 6- Outro\n"))
    if(deusMeAjude< 0 or deusMeAjude>6):
        print("Opção invalida")
    else:
        votos.append(deusMeAjude)
        for i in range (1,len(sistema)):
            if(votos[cont]==i):
                sistema[i-1] += 1
        cont += 1
maior = 0
for i in range (0,len(sistema)):
    if (i == 0):
        i = maior
    if (sistema[i] > maior):
        maior = i
sistema[0] -= 1 #arrumando uma gambiarra
total = len(votos) - 2
if(total != 0):
    print(f"Sistema Operacional     Votos               %"   )
    print(f"-------------------     -----------         ------")
    print(f"Windows Server          {sistema[0]}        {(sistema[0]*100)/total}%")
    print(f"Unix                    {sistema[1]}        {(sistema[1]*100)/total}%")
    print(f"Linux                   {sistema[2]}        {(sistema[2]*100)/total}%")
    print(f"Netware                 {sistema[3]}        {(sistema[3]*100)/total}%")
    print(f"Mac                     {sistema[4]}        {(sistema[4]*100)/total}%")
    print(f"Outro                   {sistema[5]}        {(sistema[5]*100)/total}%")
    print(f"-------------------     -----------         ------")
    print(f"Total:                  {total}")
    if(maior == 0):
        print(f"O sistema Operacional mais votado foi o Windows Server, com {sistema[0]} votos, correspondendo a {(sistema[0]*100)/total}% dos votos")
    if(maior == 1):
        print(f"O sistema Operacional mais votado foi o Unix, com {sistema[1]} votos, correspondendo a {(sistema[1]*100)/total}% dos votos")
    if(maior == 2):
        print(f"O sistema Operacional mais votado foi o Linux, com {sistema[2]} votos, correspondendo a {(sistema[2]*100)/total}% dos votos")
    if(maior == 3):
        print(f"O sistema Operacional mais votado foi o Netware, com {sistema[3]} votos, correspondendo a {(sistema[3]*100)/total}% dos votos")
    if(maior == 4):
        print(f"O sistema Operacional mais votado foi o Mac, com {sistema[4]} votos, correspondendo a {(sistema[4]*100)/total}% dos votos")
    if(maior == 5):
        print(f"O sistema Operacional mais votado foi o Outro, com {sistema[5]} votos, correspondendo a {(sistema[5]*100)/total}% dos votos")
else:
    print("Não houve votos válidos")