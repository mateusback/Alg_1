import random
import string

# 1.
def numInt():
    num = int(input("Informe um valor inteiro: "))
    return (num)

# 2.
def numRand(n):
    numR = random.randint(1, n)
    return (numR)

# 3.
def mes(n):
    if (n == 1):
        return ("Janeiro")
    elif (n == 2):
        return ("Fevereiro")
    elif (n == 3):
        return ("Março")
    elif (n == 4):
        return ("Abril")
    elif (n == 5):
        return ("Maio")
    elif (n == 6):
        return ("Junho")
    elif (n == 7):
        return ("Julho")
    elif (n == 8):
        return ("Agosto")
    elif (n == 9):
        return ("Setembro")
    elif (n == 10):
        return ("Outubro")
    elif (n == 11):
        return ("Novembro")
    elif (n == 12):
        return ("Dezembro")
    else:
        return ("Mês invalido")

# 4.
def quadrado(x):
    q = x * x
    return (q)

def retangulo(b, h):
    ret = b * h
    return (ret)

def triangulo(b, h):
    tri = (b * h) / 2
    return (tri)

def trapezio(B, b, h):
    trap = ((B + b) * h) / 2
    return (trap)

# 5.
def fatRep(n):
    if (n == 1 or n == 0):
        return (1)
    else:
        fat = 1
        while (n > 1):
            fat = fat * n
            n -= 1
        return (fat)

# 6.
def fat(n):
    if (n == 1 or n == 0):
        return (1)
    else:
        return (n * fat(n-1))

#7.
def vetMaior(vet):
    maior = vet[0]
    for i in range(1, len(vet)):
        if (vet[i] > maior):
            maior = vet[i]
    return (maior)

#8.
def vetMenor(vet):
    menor = vet[0]
    for i in range(1, len(vet)):
        if (vet[i] < menor):
            menor = vet[i]
    return (menor)

#9.
def vetMed(vet):
    soma = 0
    for i in range(0,len(vet)):
        soma += vet[i]
    return (soma/len(vet))

#10
def vetDobro(vet):
    vet2 = [0] * len(vet)
    for i in range(0,len(vet)):
        vet2[i] = vet[i] * 2
    return(vet2)

#11
def data(data):
    data = list(data)
    diat = data[0] + data[1]
    mest = data[3] + data [4]
    anot = data[9] + data[7] + data[8] + data[9]
    stri = diat + " de " + mes(int(mest)) + " de " + anot
    return(stri)

#12
def invInt(num):
    aux=0
    inv=0

    while(num > 0):
        aux=num % 10
        inv=inv * 10 + aux
        num=num // 10  
    return(inv) 

#13.
def invStr(texto):
    tex = texto[::-1]
    return(tex)

#14.   
def vogais(stri):
    stri = list(stri)
    vogais = 0
    for i in range(0, len(stri)):
        if(stri[i] == 'a' or stri [i] == 'e' or stri [i] =='o' or stri [i] =='u'):
            vogais += 1
    return(vogais)

#15
def embaralharRep(stri):
    stri = list(stri.lower())
    emb = [''] * len(stri)
    for i in range(0,len(stri)):
        emb[i] = stri[random.randint(0,len(stri)-1)]
    return (emb)

#16
def embaralhar(stri):
    stri = list(stri.lower())
    emb = [''] * len(stri)
    aleatorio = []
    while len(aleatorio) != len(stri):
        r = random.randint(0, len(stri)-1)
        if (r not in aleatorio):
            aleatorio.append(r)
    for i in range(0,len(stri)):
        emb[i] = stri[aleatorio[i]]
    return (emb)

#17
def salario(cargo):
    if(cargo.lower() == "gerente"):
        return(0.10)
    elif(cargo.lower() == "engenheiro"):
        return(0.20)
    elif(cargo.lower() == "tecnico"):
        return(0.30)
    else:
        return(0.05)

