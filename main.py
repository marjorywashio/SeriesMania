from interface import Interface

interface = Interface()

opcao = ""
while opcao != 0:
    interface.logotipo()
    interface.mostraMenu()
    opcao = interface.selecionaOpcao([1, 2, 0])
    interface.limpaTela()

    # Tela de cadastro de filmes
    if opcao == 1:
        interface.mostraCadastro()
        print()
        opcao = ""
    # Tela de lista de filmes
    elif opcao == 2:
        interface.mostraLista()
        opcao = ""
        interface.limpaTela()