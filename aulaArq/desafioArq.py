import random

while(True):
    print("1 - Mostrar números")
    print("2 - Mostrar relatório")
    print("3 - Inserir número aleatório")
    print("4 - Inserir número úsuario")
    print("5 - Sair")
    opc = int(input(""))
    if(opc == 1):
        arq = open("C:/Users/Aluno/Desktop/aulaArq/texto.txt", "r")
        cnt = arq.readlines()
        for i in range (0,len(cnt)):
            print(cnt[i])
        arq.close()
    elif(opc == 2):
        arq = open("C:/Users/Aluno/Desktop/aulaArq/texto.txt", "r")
        cnt = arq.readlines()

        '''
        Qual o maior número dos dados
        Qual a média dos valores
        Quantos números pares
        '''

        maior = int(cnt[0])
        soma = 0
        par = 0
        for i in range(0, len(cnt)):
            # transformando cada linha em int para utiliza-las
            num = int(cnt[i])
            if (num > maior):
                maior = num
            soma += num
            if (num % 2 == 0):
                par += 1

        print("O maior é:", maior)
        print("A média dos números do arquivo é:", soma/len(cnt))
        print("A quantidade de números pares é:", par)
        print("A quantidade total de números é:", len(cnt))

        arq.close()
    elif(opc == 3):
        arq = open("C:/Users/Aluno/Desktop/aulaArq/texto.txt", "a")
        n = random.rand(1,1000)
        arq.write(str(n) + "\n")

        arq.close()
    elif(opc == 4):
        arq = open("C:/Users/Aluno/Desktop/aulaArq/texto.txt", "a")
        n = input("Informe o número para adicionar no txt: ")
        arq.write(n + "\n")
        arq.close()
    elif(opc == 5):
        break
    else:
        print("Opção invalida")
