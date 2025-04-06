from conexao import Conexao
from menu import exibir_menu

def listar_cursos(con):
    with con.cursor() as cur:
        cur.execute("SELECT id, nome_completo FROM tb_cursos ORDER BY id;")
        cursos = cur.fetchall()
        print("\nCursos disponíveis:")
        for curso in cursos:
            print(f"{curso[0]} - {curso[1]}")
    return cursos

def inserir_aluno(con):
    nome = input("Nome do(a) aluno(a): ")
    rga = input("RGA do(a) aluno(a): ")
    listar_cursos(con)
    curso_id = int(input("Digite o ID do curso: "))

    with con.cursor() as cur:
        cur.execute("SELECT Inserir_Aluno(%s, %s, %s);", (nome, rga, curso_id))
        aluno_id = cur.fetchone()[0]
        con.commit()
        print(f"Aluno inserido com sucesso! ID: {aluno_id}")

def listar_alunos(con):
    with con.cursor() as cur:
        cur.execute("""
            SELECT a.id, a.nome, a.rga, c.nome_completo
            FROM tb_alunos a
            LEFT JOIN tb_cursos c ON a.curso_id = c.id
            ORDER BY a.id;
        """)
        alunos = cur.fetchall()
        print("\nAlunos cadastrados:")
        for aluno in alunos:
            print(f"{aluno[0]} - {aluno[1]} (RGA: {aluno[2]}) - Curso: {aluno[3]}")

def main():
    with Conexao() as con:
        while True:
            opcao = exibir_menu()
            if opcao == '1':
                inserir_aluno(con)
            elif opcao == '2':
                listar_alunos(con)
            elif opcao == '9':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

if __name__ == '__main__':
    main()
