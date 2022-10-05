#1

#a
for num in range(1, 101):
    print("Linha:", num)


#b
for num in range(100, -1, -1):
    print("Linha:", num)

#c
for num in range(2, 101, 2):
    print("Linha:", num)

#d
for num in range(1, 101, 2):
    print("Linha:", num)

#e
soma=0
for num in range(1, 101):
    soma=soma + num
print("Soma dos valores de 1 a 100:", soma)

#f
x=int(input("Apresente o valor de x: "))
y=int(input("Apresente o valor de y: "))
if(x < y):
    soma=0
    for num in range(x, y+1):
        soma=soma + num
    print("Soma dos valores de", x, "a", y, ":", soma)
else:
    print("O valor de x deve ser menor que y")

#g
j=int(input("Apresente o valor do fatorial: "))
fatorial=1
for num in range(1, j+1):
    fatorial=fatorial * num
print("O fatorial de", j, "é:", fatorial)

#2
valor=[]
for i in range(0, 5):
    valor.append(int(input("Informe um valor: ")))
print("Dentre os númeors informados, o maior foi:", max(valor))
maior=-99999999999999999999999999999999999999
for i in range(5):
    n=float(input("Digite um número:"))
if n > maior:
    maior=n
i += 1
print("O maior número é:", maior)

#3
valor=[]
for i in range(0, 5):
    valor.append(int(input("Informe um valor: ")))
print("A soma dos valores informados é:", sum(valor))
print("A média dos valors informdos é:", sum(valor) / len(valor))
soma=0
media=0
for n in range(5):
    soma += int(input("Digite um número:"))
media=soma / 5
print("A soma é:", soma, "e a média:", media)

#4
for num in range(1, 51, 2):
    print("Linha:", num)


#5
for i in range(1, 51):
    print(i, "- R$", valor*i)

#6
a=int(input("Informe o valor: "))

for cont in range(0, 11):
    x=a * cont
print(a, "x", cont, "=", x)


#7

n1=int(input("Informe o valor inicial da tabuada: "))
n2=int(input("Informe o valor final da tabuada: "))
tabuada=int(input("Informe qual tabuada tu queres: "))

if(n2 < n1):
    swp=n1
    n1=n2
    n2=swp

resultado=0
for i in range(n1, n2+1):
    resultado=tabuada * i
print(tabuada, "x", i, "=", resultado)