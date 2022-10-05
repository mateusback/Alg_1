### Lista 08 ✅

#1
cont = 0

while(cont < 101):
    print("Contagem", cont)
    cont = cont + 1

#a
num = 1
soma = 0
while(num < 101):
    soma = soma + num
    num += 1
print("A soma dos valores de 1 a 100 é:", soma)

#b
num = 50
while(num < 101):
    print(num)
    num += 2

#c
num = 51
while(num < 101):
    print(num)
    num += 2

#d
num = 0
soma = 0
while(num < 101):
    soma = soma + num
    num += 2
print("A soma dos valores pares entre 1 e 100 é:")

#e
x = int(input("Informe o valor para começar a repetição: "))
y = int(input("Informe o valor para terminar a repetição: "))

if(x > y):
    swp = y
    y = x
    x = swp

while(x <= y):
    print(x)
    x += 1

#f
x = int(input("Informe o valor para começar a repetição: "))
y = int(input("Informe o valor para terminar a repetição: "))

if(y < x):
    swp = x
    x = y
    y = swp
z = x
soma = 0
while(x <= y):
    soma = soma + x
    x += 1
    print("O resultado da soma entre", z, "e", y , "é:", soma)

#g
x = int(input("Informe o valor para começar a repetição: "))
y = int(input("Informe o valor para terminar a repetição: "))

if(y < x):
    swp = x
    x = y
    y = swp

while(x <= y):
    if(x % 2 != 0):
        print(x)
    x += 1

#2

#a
tabu = int(input("Informe o valor da tabuada: "))
i = 1
while(i <= 10):
    resultado = tabu * i
    print(tabu, "x", i, "=", resultado)
    i += 1

#b
x = int(input("Informe o valor para começar: "))
y = int(input("Informe o valor para terminar: "))
tabu = int(input("Informe o valor da tabuada:"))

if(y < x):
    swp = x
    x = y
    y = swp

while(x <= y):
    resultado = tabu * x
    print(tabu, "x", x, "=", resultado)
    x += 1


#3
fat = int(input("Informe o valor da fatorial:"))
resultado = 1
fat2 = fat
while(fat >= 1):
    resultado = fat * resultado
    fat -= 1
print("O fatorial de", fat2, "=", resultado)

#4
n = int(input("Informe o valor de n:"))

resultado = 0
i = 1
while(i <= n):
    resultado = resultado + (1 / i)
    i += 1
print("O valor de H é:", resultado)

#5

#a
import random
b=0
a=random.randint(1, 10)
while(b != a):
    b=int(input("Tente adivinhar o número sorteado: "))
print("Parabains, fim do prograima!")

#b
import random
b=0
a=random.randint(1, 10)
cont=0
while(b != a):
    b=int(input("Tente adivinhar o número sorteado: "))
    cont += 1
print("Parabains, fim do prograima em", cont, "tentatoivas")

#c
import random
b=0
a=random.randint(1, 10)
while(b != a):
    a=random.randint(1, 10)
    b=int(input("Tente adivinhar o número sorteado: "))
print("Parabains, fim do prograima!")

#d
import random
b=0
a=random.randint(1, 10)
cont=0

while(b != a):
    a=random.randint(1, 10)
    b=int(input("Tente adivinhar o número sorteado: "))
    cont += 1

print("Parabains, fim do prograima em", cont, "tentatoivas")

#6
import math
loop=0
while(loop != 4):
    print("")
    print("====== Menu Principal ======")
    print("1. Par ou ímpar?")
    print("2. Potência X^Y")
    print("3. Raiz quadrada")
    print("4. Sair")
    print("============================")
    loop=int(input("Informe a escolha: "))

if(loop == 1):
    vl1=int(input("Informe um valor: "))
    if(vl1 % 2 == 0):
        print("O valor i   nformado é par")
    else:
        print("O valor informado é ímpar")

elif(loop == 2):
    vl1=int(input("Informe o valor de X: "))
    vl2=int(input("Informe o valor de Y: "))
    print("A potência de X^Y é:", vl1 ** vl2)

elif(loop == 3):
    vl1=int(input("Informe um valor:"))
    print("A raiz quadrada de", vl1, "é:", math.sqrt(vl1))

elif(loop >= 5 or loop >= 0):
    print("Opção inválida")

print("Fim do programa")

#
loop=0
while(loop != 4):
    print("")
    print("====== Menu Principal ======")
    print("1. Fazer a tabuada do 1 ao 10 para um número X")
    print("2. Apresentar os múltiplos de X entre 1 e 100 ")
    print("3. Apresentar a soma dos números de 1 a 100 ")
    print("4. Sair")
    print("============================")
    loop=int(input("Informe a escolha: "))

if(loop == 1):
    tabu=int(input("Informe o valor da tabuada: "))
    for i in range(1, 11):
        print(i, "x", tabu, "=",i*tabu)

elif(loop == 2):
    mult=int(input("Informe o valor: "))
    for i in range(1, 101):
        if(i % mult == 0):
            print(i)

elif(loop == 3):
    soma=0
    for i in range(1, 101):
        soma += i
    print("A soma dos valores entre 1 e 100 é:", soma)

elif(loop >= 5 or loop <= 0):
    print("Opção inválida")

print("Fim do programa")

#8
i=1
j=1
total=0
while (j != 0):
    j=float(input(f"Produto "+str(i)+": R$ "))
    total += j
    i += 1
print("Total: R$", total)
troco=float(input("Dinheiro: R$ "))
print("Troco: R$", troco - total)

#9
import math
temp=[]
for i in range(1, 8):
    temp.append(float(input("Informe a temperatura: ")))
    print("A média das temperaturas é:", sum(temp)/len(temp))
    print("A maior temperatura foi:", max(temp))
    print("A menor temperatura foi:", min(temp))

#10
i=0
cont=0
total=0

while(i != -1):
    i=int(input("Informe um valor: (digite -1 para parar): "))
    total += i
    cont += 1
print("A média dos valores informados é:", total/cont)
 
#11
quantCd=int(input("Informe a quantidade de CDs comprados: "))
valor=[]

for i in range(1, quantCd+1):
    valor.append(int(input("Iforme o valor do CD: ")))

print("O valor total gasto em CDs foi de: R$", sum(valor))
print("A média de valores entre os CDs é: R$", sum(valor)/quantCd)


#12 - null

#13
nome=input("Informe o nome do atleta: ")
sum=0
maiornota=-9999999999999999999999999999999999999999999999
menornota=9999999999999999999999999999999999999999999999

for i in range(1, 8):
    nota=float(input("Nota:"))
    sum += nota
    if(nota < menornota):
        menornota=nota
    elif(nota > maiornota):
        maiornota=nota

print("Resultado Final:")
print("Atleta:", nome)
print("Melhor nota:", maiornota)
print("Pior nota:", menornota)
print("Média>", sum/7)

#14
an=80000
bn=200000
anos=0

while (an < bn):
    an += an * 0.03
    bn += bn * 0.015
    anos += 1
print("A quantidade de habitantes entre as duas cidades será a mesma em:", anos, "anos")

#15
num=int(input("Digita um número ai: "))
numSalvo=num
lembrar=0
inv=0

while(num > 0):
    lembrar=num % 10
    inv=inv * 10 + lembrar
    num=num // 10

print("numero digitado:", numSalvo)
print("numero inverso:", inv)
