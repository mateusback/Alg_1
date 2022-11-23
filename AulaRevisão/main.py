import blib

#classe é um molde
#um objeto é uma instancia de uma classe,
disciplina = blib.pegarDados()

blib.salvar(disciplina)

x = blib.lerDados()

#presta atenção em como exibir um objeto ai
for i in range(0, len(x)):

    print("Código", x[i].codigo)
    print("Nome:", x[i].nome)
    print("Carga Horária:", x[i].ch)
    print("Professor:", x[i].professor)
    print("Carga Horária Relógio:", x[i].chr)
