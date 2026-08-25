import sqlite3


def conectar_banco():
    return sqlite3.connect("atleta360.db")


def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS atletas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT,
        categoria TEXT,
        posicao TEXT
    )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_atleta():
    nome = input("Nome do atleta: ")
    data_nascimento = input("Data de nascimento: ")
    categoria = input("Categoria: ")
    posicao = input("Posição: ")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO atletas (nome, data_nascimento, categoria, posicao)
    VALUES (?, ?, ?, ?)
    """, (nome, data_nascimento, categoria, posicao))

    conexao.commit()
    conexao.close()

    print("\nAtleta cadastrado com sucesso!")


def listar_atletas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM atletas")
    atletas = cursor.fetchall()

    conexao.close()

    print("\n--- ATLETAS CADASTRADOS ---")

    if len(atletas) == 0:
        print("Nenhum atleta cadastrado.")
    else:
        for atleta in atletas:
            print(f"ID: {atleta[0]}")
            print(f"Nome: {atleta[1]}")
            print(f"Data de nascimento: {atleta[2]}")
            print(f"Categoria: {atleta[3]}")
            print(f"Posição: {atleta[4]}")
            print("---------------------------")


def atualizar_atleta():
    id_atleta = input("Digite o ID do atleta que deseja atualizar: ")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM atletas WHERE id = ?",
        (id_atleta,)
    )

    atleta = cursor.fetchone()

    if atleta is None:
        print("\nNenhum atleta encontrado com esse ID.")
        conexao.close()
        return

    print("\nDados atuais:")
    print(f"Nome: {atleta[1]}")
    print(f"Data de nascimento: {atleta[2]}")
    print(f"Categoria: {atleta[3]}")
    print(f"Posição: {atleta[4]}")

    nome = input("\nNovo nome: ")
    data_nascimento = input("Nova data de nascimento: ")
    categoria = input("Nova categoria: ")
    posicao = input("Nova posição: ")

    cursor.execute("""
    UPDATE atletas
    SET nome = ?,
        data_nascimento = ?,
        categoria = ?,
        posicao = ?
    WHERE id = ?
    """, (
        nome,
        data_nascimento,
        categoria,
        posicao,
        id_atleta
    ))

    conexao.commit()
    conexao.close()

    print("\nAtleta atualizado com sucesso!")


def excluir_atleta():
    id_atleta = input("Digite o ID do atleta que deseja excluir: ")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM atletas WHERE id = ?",
        (id_atleta,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("\nAtleta excluído com sucesso!")
    else:
        print("\nNenhum atleta encontrado com esse ID.")

    conexao.close()


def menu():
    
        print("\n=================================")
        print("           ATLETA360")
        print("       Gestão de Atletas")
        print("=================================")
        print("1 - Cadastrar atleta")
        print("2 - Listar atletas")
        print("3 - Atualizar atleta")
        print("4 - Excluir atleta")
        print("0 - Sair")
        print("=================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_atleta()

        elif opcao == "2":
            listar_atletas()

        elif opcao == "3":
            atualizar_atleta()

        elif opcao == "4":
            excluir_atleta()

        elif opcao == "0":
            print("\nAtleta360 encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


criar_tabela()
menu()