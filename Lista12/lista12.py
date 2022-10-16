
import acoes

num = acoes.numInt()
print(num)

numR = acoes.numRand(num)
print(numR)

mes = acoes.mes(numR)
print(mes)

fat = acoes.fatRep(num)
print(fat)

fat2 = acoes.fat(num)
print(fat2)

vetor = [1,5,67,234,72,123,77,874]

maior = acoes.vetMaior(vetor)
menor = acoes.vetMenor(vetor)
print(maior,menor)
med = acoes.vetMed(vetor)
print(med)
vet2 = acoes.vetDobro(vetor)
print(vet2)

inv = acoes.invInt(num)
print(inv)

data = "16/10/2022"
data2 = acoes.data(data)
print(list(data))
print(data2)
tex = acoes.invStr("Olá, Marilene")
print(tex)
vogais = acoes.vogais("Mateus")
print(vogais)

emb = acoes.embaralharRep("Mateus")
print(emb)

emb = acoes.embaralhar("Mateus")
print(emb)

#17
salario = float(input("Informe seu salário: "))
cargo = input("Iforme seu cargo: ")
diferenca = salario * acoes.salario(cargo)
print("Seu novo salário é: R$", salario + diferenca)
print("Seu antigo sálario era: R$", salario)
print("A diferença entre eles é de: R$", diferenca)
