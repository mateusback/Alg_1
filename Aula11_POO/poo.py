#Data
class Data:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0


class Aluno:
    def __init__(self): #uma função que inicia a minha classe - "self"
        self.nome = ""
        self.idade = 0
        self.email = ""
        self.sexo = False #False = Feminino
        self.datanascimento = Data()


data1 = Data()
data1.dia = int(input("Informe o dia: "))
data1.mes = int(input("Informe o mês: "))
data1.ano = int(input("Informe o ano: "))

print(f"Data informada: {data1.dia}/{data1.mes}/{data1.ano}")

a = Aluno()
a.nome = "Fulano"
a.idade = 45
a.email = "faluno33@gmail.com"
a.sexo = True
a.datanascimento.dia = 25
a.datanascimento.mes = 10
a.datanascimento.ano = 2022

print("Nome:", a.nome)

b = Aluno()
b.nome = "Ciclano"
b.idade = 60
b.email = "ciclano66@gmail.com"
b.sexo = False

print(f"Nome: {b.nome}\nIdade: {b.idade}\nE-mail: {b.email}\nSexo: {b.sexo}")
