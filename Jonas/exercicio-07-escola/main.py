from Aluno import Aluno
from Curso import Curso
from Escola import Escola

def main():
    aluno1 = Aluno("Jonas", 12345)
    aluno2 = Aluno("João", 67890)

    curso1 = Curso("Matemática", 20241)
    curso2 = Curso("Geografia", 20242)
    curso3 = Curso("História", 20243)

    curso1.adicionar_aluno(aluno1)
    curso2.adicionar_aluno(aluno1)
    curso1.adicionar_aluno(aluno2)
    curso2.adicionar_aluno(aluno2)

    escola = Escola("Instituto Federal do Amazonas")
    escola.adicionar_curso(curso1)
    escola.adicionar_curso(curso2)
    escola.adicionar_curso(curso3)

    escola.mostrar_cursos()

    print("")

    curso1.mostrar_alunos()
    
if __name__ == '__main__':
    main()