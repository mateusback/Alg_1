import mysql.connector

banco = mysql.connector.connect(
	host='localhost', #local do BD
	user='root', #usario do BD
	password='',  #senha do BD
	database='algoritimos') #nome do BD
print("Database connection made!")


cursor = banco.cursor() #criando o cursor

#Esses comandos servem para inserir, alterar e deletar.
sql = "INSERT INTO disciplina VALUES (%s ,%s,%s,%s)"
valores1 = (None, "Algoritimos", 160, "Rafael")
valores2 = (None, "Eng. de Software", 100, "André")
valores3 = (None, "Banco de Dados", 200, "Hélio")

cursor.execute(sql, valores1) #executando os comandos
cursor.execute(sql, valores2)
cursor.execute(sql, valores3)

nome = input("Informe o nome da matéria: ")
ch = int(input("Informe a carga horária: "))
professor = input("Informe o nome do professor: ")

valores4 = (None, nome, ch, professor)
cursor.execute(sql, valores4)

banco.commit()  # salvando as alterações

cursor.execute("SELECT * FROM disciplina")

resultados = cursor.fetchall()

for i in range (0, len(resultados)):
  print(resultados[i])

cursor.close() #fechando o cursor
banco.close() #fechando o banco