#1
num = int(input("Informe um numero"))
print("O antecessor do numero", num,"eh:", num-1, "e seu sucessor eh:", num+1)

#2
num1 = int(input("Informe um numero"))
num2 = int(input("Informe outro numero"))
soma = num1+num2
print("A soma dos numeros eh",soma)

#3
num1 = int(input("Informe um numero"))
num2 = int(input("Informe outro numero"))
num3 = int(input("Informe mais um numero"))
produto = num1 * num2 * num3
print("o produto dos numeros eh", produto)

#4
nota1 = float(input("Informe a media do primeiro bimestre"))
nota2 = float(input("Informe a media do segundo bimestre"))
nota3 = float(input("Informe a media do terceiro bimestre"))
nota4 = float(input("Informe a media do quarto bimestre"))
media = (nota1 + nota2 + nota3 + nota4)/4
print("A sua media de notas eh:", media)

#5
metros = float(input("informe a quantidade de metros"))
centimetros = metros*100
print(metros, "metros sÃƒÂ£o", centimetros, "centimetros")

#6
raio =float(input("informe o raio do circulo"))
area = 3.14 * (raio**2)
print("a area do circulo eh:", area)

#7
lado = float(input("Informe a medida do lado do quadrado"))
area = lado * lado
print("A area do quadrado eh:", area)
perimetro = lado * 4
print("o perimetro do quadrado eh:", perimetro)

#8
salarioH = float(input("informe o quanto vocÃƒÂª recebe por hora"))
horasTrab = int(input("informe a quantidade de horas trabalhadas por dia"))
salarioD = salarioH * horasTrab
salarioM = salarioD * 20
print("por dia, voce recebe:", salarioD, "e por mes, voce recebe:",salarioM)


#9
tempF = int(input("Informe a temperatura em Farenheit: "))
tempC = 5 * (tempF - 32) / 9
print("A temperatura informa ÃƒÂ© a mesma que: ", tempC ,"em Graus Celsius")

#10
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))
imc = peso / altura ** 2
print("De acordo com seu peso e altura, seu IMC ÃƒÂ©:",imc)

#11
print("Dada a equaÃƒÂ§ÃƒÂ£o: ax2+bx+c=0")
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
calc = (-b + ((b**2- 4 * a *c )**(0.5))) / 2 * a
print(calc)


#12
nome = input("Informe o nome do produto: ")
valor = float(input("Informe o valor do produto: "))
desconto = float(input("Informe o desconto: "))
descontoP = desconto + desconto/100
valorF = valor - descontoP
descontoTotal = valorF - descontoP

print("Produto:", nome)
print("-------------------")
print("Valor: RS", valor)
print("Desconto: RS", descontoTotal)
print("-------------------")
print("Valor Final: RS", valorF)
print("-------------------")


#13
tamanho = float(input("Informe quantos metros quadrados: "))
litros = tamanho / 3
latas = litros / 18
quantia = int(latas + 1)
precoLata = 120
precoTotal = quantia * precoLata 

print("A quantidade de latas a serem utilizadas Ã©: ",quantia) 
print("O valor total das latas serÃ¡: ",precoTotal)


#14
salarioH = float(input("Quando voce ganha por Hora? "))
horas = int(input("Quantas horas trabalhou no mes? "))
salarioBruto = salarioH * horas
imposto = salarioBruto * 0.075
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.01
salarioL = salarioBruto - imposto - inss - sindicato

print("+ Seu salÃ¡rio bruto no mÃªs Ã© de R$",salarioBruto)
print("- IR (7.5%): R$",imposto)
print("- INSS (8%): R$",inss)
print("- Sindicado (1%): R$",sindicato)
print("= SalÃ¡rio LÃ­quido: R$",salarioL)