arq = open("C:/Users/Aluno/Desktop/aulaArq/texto.txt", "r")  # Função

print("Nome: ", arq.name)
print("Modo: ", arq.mode)
print("Fechado? ", arq.closed)

'''cnt = arq.readline()  # jogando o conteudo da primeira linha na variavel cnt
print(cnt)
cnt = arq.readline()  # jogando o conteudo da segunda linha na variavel cnt
print(cnt)
cnt = arq.readline()  # jogando o conteudo da terceira linha na variavel cnt
print(cnt)'''

cnt = arq.readlines() # joga as linhas do txt em um vetor
print(cnt)
for i in range(0, len(cnt)):
    print(cnt[i])


arq.close()  # procedimento para fechar o arquivo

print("Fechado? ", arq.closed)
