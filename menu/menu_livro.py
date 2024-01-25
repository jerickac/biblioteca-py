from livro.livro_buscar import buscarPorCodigo
from livro.livro_editar import editarLivro
from livro.livro_listar import listarLivros
from livro.livro_deletar import deletarLivro
from livro.livro_registrar import registrarLivro

def menu() -> None:
    while True:
        print("-----Bem-vindo ao menu-----")
        print("1 - Adicionar Livro")
        print("2 - Editar Livro")
        print("3 - Deletar Livro")
        print("4 - Buscar por código")
        print("5 - Listar Livro")
        print("6 - Sair")
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            titulo = input("Digite o titulo: ")
            autor = input("Digite o autor: ")
            registrarLivro(titulo, autor)

        elif opcao == '2':
            codigo = int(input("Digite o código: "))
            titulo = input("Digite o título: ")
            autor = input("Digite o autor: ")
            editarLivro(codigo, titulo, autor)

        elif opcao == '3':
            codigo = int(input("Digite o código do livro"))
            deletarLivro(codigo)

        elif opcao == '4':
            codigo = int(input("Digite o código do livro"))
            buscarPorCodigo(codigo)

        elif opcao == '5':
            listarLivros()

        elif opcao == '6':
            break

        else:
            print("Opção inválida")