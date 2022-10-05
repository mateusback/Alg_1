# Exercício 1:
import random

print("== Menu de Opções ==")
print("1. Somar 2 números")
print("2. Potência Y de um número X (x^y)")
print("3. Raiz quadrada de X")
print("4. Gerar um número aleatório")
escolha = input("== Opção escolhida: ")

if(escolha=="1"):
    n1 = int(input("Informe o primeiro valor: "))
    n2 = int(input("Informe o segundo valor: "))
    soma = n1 + n2
    print("A soma dos valores apresentados é:", soma)

elif(escolha == "2"):
    n1 = int(input("Informe o valor de X: "))
    n2 = int(input("Informe o valor de Y: "))
    pot = n1**n2
    print("O resultado da potência é:", pot)

elif(escolha == "3"):
    n1 = int(input("Informe o valor de X: "))
    raiz = n1 ** 0.5
    print("O resultado da raiz é:", raiz)

elif(escolha == "4"):
    print("O número sorteado é:", random.randint(1,10000000000000000000000000000000000000000000000000000000000000))

else:
    print("digita certo ae")

# Exercício 2:
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))
imc = peso/altura**2
if(imc<18.5):
    print("Baixo peso")
elif(imc<=18,5 and imc>=24.9):
    print("Peso normal")
elif(imc<=25 and imc>=29.9):
    print("Pré-obesidade")
elif(imc<=30 and imc>=34.9):
    print("Obesidade Grau I")
elif(imc<=35 and imc>=39.9):
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")


# Exercício 3:
salario = float(input("Infrome seu salário: "))

if(salario<=710.00):
    aumento = salario * (20/100)
    novosalario = aumento + salario
    print("Seu salário era:", salario)
    print("O percentual do reajuste foi de 20%")
    print("O valor aumento foi:", aumento)
    print("Seu salário com o reajuste é:", novosalario)
    

elif(salario >= 710.01 and salario <= 1000.0):
    aumento = salario * (15/100)
    novosalario = aumento + salario
    print("Seu salário era:", salario)
    print("O percentual do reajuste foi de 15%")
    print("O valor aumento foi:", aumento)
    print("Seu salário com o reajuste é:", novosalario)

elif(salario >= 1000.01 and salario <= 25000.00):
    aumento = salario * (10/100)
    novosalario = aumento + salario
    print("Seu salário era:", salario)
    print("O percentual do reajuste foi de 10%")
    print("O valor aumento foi:", aumento)
    print("Seu salário com o reajuste é:", novosalario)
else:
    aumento = salario * (5/100)
    novosalario = aumento + salario
    print("Seu salário era:", salario)
    print("O percentual do reajuste foi de 5%")
    print("O valor aumento foi:", aumento)
    print("Seu salário com o reajuste é:", novosalario)

# Exercício 4:
import random

print("== Menu de Opções ==")
print("1. Gerar um número aleatório entre X e Y")
print("2. X é par ou ímpar?")
print("3. Valor R$X com Y% de desconto")

op = int(input("== Opção escolhida: "))

if (op==1):
    x = int(input("Informe o valor de x: "))
    y = int(input("Informe o valor de y: "))
    print("O número sorteado é:", random.randint(x,y))
elif(op==2):
    x = int(input("Informe o valor de x: "))
    if (x%2) == 0:
        print("Par")
    else:
        print("Ímpar")
elif(op==3):
    x = float(input("Informe o valor de x: "))
    y = int(input("Informe o valor de y: "))
    desconto = x * (y/100)
    valor = x - desconto
    print("Valor R$",x,"com",y,"% de desconto é:",valor)
else:
    print("Digite uma opção valida")

# Exercício 5:

kgMaca = float(input("Informe a quantidade de Kg de maçãs compradas: "))
kgMorango = float(input("Informe a quantidade de Kg de morangos comprados: "))
totalKg = kgMorango + kgMaca
vlMorango = 0.0
vlMaca = 0.0

if(kgMaca>5):
    vlMaca = kgMaca * 3.50
    
if(kgMorango>5):
    vlMorango = kgMorango * 7.90

if(kgMaca<=5 and kgMorango<=5):
    vlMaca = kgMaca * 3.90
    vlMorango = kgMorango * 8.90

totalVl = vlMaca + vlMorango

if(totalVl>25.0 or totalKg>8):
    compra = totalVl - totalVl * (7/100)
    print("O valor da compra, com 7% de desocnto, é de: R$", compra)
elif(totalVl < 25.0 or totalKg <8):
    print("O valor da compra é de: R$", totalVl)
