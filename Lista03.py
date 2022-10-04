
"""
#1
num = int(input("Insira um nÃºmero: "))
if(num > 0):
    print("O nÃºmero Ã© positivo")
else:
    print("O nÃºmero Ã© negativo")
 

#2
n1 = int(input("Digite o valor do primeiro nÃºmero: "))
n2 = int(input("Digite o valor do segundo nÃºmero: "))
if (n1 > n2):
    print("O primeiro Ã© maior:",n1)
else:
    print("O segundo Ã© maior:",n2)
  

#3
idade = int(input("Informe sua idade: "))
if (idade > 18):
    print("Entrada permitida!")
else:
    print("Entrada negada!")
      

#4
nota1 = int(input("Informe sua nota do trabalho: "))
nota2 = int(input("Insira sua nota da prova: "))
media = (nota1 + nota2) / 2 
if(media >= 60 ):
    print("Aprovado!")
else:
    print("Reprovado!")
 

#5
conceito = input("Informe o coneceito na disciplina: ")
if(conceito != 'D'):
    print("Aprovado!")
else:
    print("Reprovado")
 

#6
salario = float(input("Informe seu salrÃ¡rio: "))
quantia = int(salario // 1212.00) 
if(salario < 1212.00):
    print("VocÃª recebe menos que um salÃ¡rio mÃ­nimo R$",salario)
else:
    print("VocÃª recebe em salÃ¡rios mÃ­nimos:",quantia)

  
#7
sexo = input("Informe seu gÃªnero: ")
if(sexo == 'F'):
    print("Feminino!")
else:
        print("Masculino!")


#8
idade = int(input("Informe sua idade: "))
if(idade >= 18):
    nome = input("Insira seu nome: ")
    print("Bem vindo",nome)
else:
    print("Entrada nÃ£o permitida!")


#9
idade = int(input("Informe sua idade: "))
if(idade >= 18):
    salario = float(input("Informe seu salÃ¡rio: R$"))
    aumento = salario * (5 / 100)
    atual = salario + aumento
    print("ParabÃ©ns, vocÃª recebeu um aumento de 5% e agora recebe: R$",atual)
else:
    print("CÃ¡lculo nÃ£o permitido.")
   
#10(nÃ£o ficou completa)
num = int(input("Insira um nÃºmero:"))
if(num < 100):
    print("NÃºmero no intervalo definido!")
else:
    print("NÃºmero fora do intervalo!!!")
     """

#11
num = int(input("Insira o nÃºmero:"))
if(num > ):