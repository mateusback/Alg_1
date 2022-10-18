#1
from ctypes import create_unicode_buffer


def nomes(arquivo):
    arq = open(arquivo.lower() + ".txt", 'a')
    nome = input("Informe um nome: ")
    arq.write(nome + "\n")
    arq.close()

#2
def leitura(arquivo):
    arq = open(arquivo.lower() + ".txt", 'r')
    ctu = arq.readlines()
    for i in range(0,len(ctu)):
        print(ctu[i])
    arq.close()

#3
def dados(arquivo):
    arq = open(arquivo.lower() + ".txt", 'a')
    nome = input("Informe seu nome:")
    email = input("Informe seu e-mail: ")
    salario = input("Informe seu salário: ")
    arq.write(nome +", "+ email +", "+salario +"\n")
    arq.close()

#4
def leituraDados(arquivo):
    arq = open(arquivo.lower() + ".txt", 'r')
    ctu = arq.readlines()
    for i in range(0,len(ctu)):
        x = ctu[i].split(',')
        print("Nome:", x[0])
        print("E-mail:", x[1])
        print("Salário: R$", x[2])
    arq.close()

#5
def maiorNum(arquivo):
    ark = open(arquivo.lower() + ".txt", 'r')
    ctu = ark.readlines()
    maior =  float(ctu[0])
    for i in range(1,len(ctu)):
        x = float(ctu[i])
        if(x > maior):
            maior = x
    print(maior)
    ark.close()

def menoresQ(arquivo):
    arq = open(arquivo.lower() + ".txt", 'r')
    ctu = arq.readlines()
    cont = 0
    for i in range(0,len(ctu)):
        x = float(ctu[i])
        if(x < 0.05):
            cont += 1
    print(cont)
    arq.close()

def quantidade(arquivo):
    arq = open(arquivo + ".txt", 'r')
    ctu = arq. readlines()
    print(len(ctu))
    arq.close()

#6
def maiorNumLinha(arquivo):
    arq = open(arquivo.lower() + ".txt", 'r')
    ctu = arq.readlines()
    maior =  -999999999999999
    for i in range(0,len(ctu)):
        x = ctu[i].split()
        for i in range (0,len(x)):
            z = float(x[i])
            if(z > maior):
                maior = z
    print(maior)
    arq.close()

def menoresQLinha(arquivo):
    arq = open(arquivo.lower() + ".txt", 'r')
    ctu = arq.readlines()
    cont = 0
    for i in range(0,len(ctu)):
        x = ctu[i].split()
        for i in range (0,len(x)):
            z = float(x[i])
            if(z < 0.05):
                cont += 1
    print(cont)
    arq.close()

def quantidadeLinha(arquivo):
    arq = open(arquivo + ".txt", 'r')
    ctu = arq.readlines()
    tamanho = 0
    for i in range(0,len(ctu)):
        x = ctu[i].split()
        tamanho += len(x)
    print(tamanho)
    arq.close()

#7
def ips(arquivo):
    ark = open(arquivo + ".txt", 'r')
    ctu = ark.readlines()
    valido = [0] * len(ctu)
    invalido = [0] * len(ctu)
    for i in range(0,len(ctu)):
        x = ctu[i].split('.')
        for y in range (0,len(x)):
            if(int(x[y])<=255 and int(x[y])>=0):
                valido[i] = ctu[i]
            else:
                invalido[i] = ctu[i]
    print("IP's válidos: ")
    for i in range (0, len(valido)):
        if (not(valido[i] == 0)):
            print(valido[i])

    print("IP's inválidos: ")
    for i in range (0, len(invalido)):
        if (not(invalido[i] == 0)):
            print(invalido[i])
