import mysql.connector
import sources

def pegarDados():
    disciplina = sources.Disciplina()
    disciplina.nome = input("Informe o nome da disciplina: ")
    disciplina.ch = int(input("Informe a carga horária: "))
    disciplina.professor = input("Informe o nome do professor: ")
    disciplina.chr = (disciplina.ch*50)/60
    return disciplina


def salvar(disciplina):
    #Arquivo
    arq = open("C:/Users/Aluno/Desktop/Aula/texto.txt", "a")
    arq.write("{\n")
    arq.write("\t\"nome\": \"" + disciplina.nome + "\",\n")
    arq.write("\t\"ch\": \"" + str(disciplina.ch) + "\",\n")
    arq.write("\t\"professor\": \"" + disciplina.professor + "\",\n")
    arq.write("\t\"chr\": \"" + str(disciplina.chr) + "\"\n")
    arq.write("}\n")
    arq.close()

    #Banco
    banco = mysql.connector.connect(
	host='localhost',
	user='root',
	password='',
	database='algoritimos')

    cursor = banco.cursor()

    sql = "INSERT INTO disciplina VALUES (%s,%s,%s,%s,%s)"
    valores = (None ,disciplina.nome, disciplina.ch, disciplina.professor, disciplina.chr)
    cursor.execute(sql, valores)

    banco.commit()

    cursor.close()
    banco.close()

def lerDados():
    banco = mysql.connector.connect(
	host='localhost',
	user='root',
	password='',
	database='algoritimos')

    cursor = banco.cursor()
    cursor.execute("SELECT * FROM disciplina")

    resultados = cursor.fetchall()

    x = [sources.Disciplina()] * cursor.rowcount
    cont = 0
    for linha in resultados:
        d = sources.Disciplina()
        d.codigo = linha[0]
        d.nome = linha[1]
        d.ch = linha[2]
        d.professor = linha[3]
        d.chr = linha[4]
        x[cont] = d
        cont +=1
    cursor.close()
    banco.close()
    return(x)

        
