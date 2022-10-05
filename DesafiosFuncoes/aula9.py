import acao

#1
a = int(input("Informe o tamanho do vetor: "))
vetor = acao.criarVetor(a)

#2
acao.exibirVetor(vetor)

#3
soma = acao.somaImpares(vetor)
print("A soma dos valores impares é:", soma)

#4
acao.busca(vetor)

#5
tipo = int(input(
    f"Informe o tipo de seleção desejada:\n1 - Bolha \n2 - Seleção\n3 - Inserção\n"))
vetorOrdenado = acao.ordenar(tipo, vetor)
acao.exibirVetor(vetorOrdenado)
