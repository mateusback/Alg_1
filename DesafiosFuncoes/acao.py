import random


def criarVetor(a):  # 1
    vetor = [0] * a
    for i in range(0, len(vetor)):
        vetor[i] = random.randint(0, 200)

    return vetor


def exibirVetor(b):  # 2
    print("Vetor:")
    for i in range(0, len(b)):
        print(b[i])


def somaImpares(c):  # 3
    soma = 0
    for i in range(0, len(c)):
        if (c[i] % 2 != 0):
            soma += c[i]
    return soma


def busca(d):  # 4
    valor = int(input("Informe um valor para buscar no vetor: "))
    iValor = -1
    for i in range(0, len(d)):
        if(d[i] == valor):
            iValor = i
            break
    if(iValor >= 0):
        print("O", valor, "está no vetor na posição", iValor)
    else:
        print("O", valor, "não está no vetor")


def ordenar(tipo, vetor):
    if(tipo == 1):  # bolha
        for i in range(len(vetor)-1, 0, -1):
            for j in range(0, i):
                if (vetor[j] > vetor[j+1]):
                    aux = vetor[j+1]
                    vetor[j+1] = vetor[j]
                    vetor[j] = aux

    elif(tipo == 2):  # inserção
        for i in range(0, len(vetor)-1):
            menor = vetor[i]
            pmenor = i
            for j in range(i+1, len(vetor)):
                if(menor > vetor[j]):
                    menor = vetor[j]
                    pmenor = j
            c = vetor[i]
            vetor[i] = menor
            vetor[pmenor] = c

    elif(tipo == 3):  # seleção
        for i in range(1, len(vetor)):
            valor = vetor[i]
            j = i - 1
            while(j >= 0 and vetor[j] > valor):
                vetor[j+1] = vetor[j]
                j -= 1
            vetor[j+1] = valor
    else:
        print("Forma de ordenação invalida")
    return vetor
