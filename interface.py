import os
from db import Database

class Interface:

    def __init__(self):
        self.banco = Database("catalogoSeries.db")

    def logotipo(self):
        print()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("+     |S|e|r|i|e|s|M|a|n|i|a|     +") 
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")
        
        #Verifica se digitou algo
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas) # recursividade (chama a própria função)
            
        # Tenta converter para número
        try:
                opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
                print("Opção inválida")
                return self.selecionaOpcao(opcoesPermitidas)
        
        # Verifica se a opção selecionada é válida
        if opcaoSelecionada not in opcoesPermitidas:
                print("Opção inválida")
                return self.selecionaOpcao(opcoesPermitidas)

        # Retorna o valor selecionado pelo usuário
        return opcaoSelecionada
    
    def mostraMenu(self):
        print("1 - Cadastrar série")
        print("2 - Listar séries")
        print("0 - Sair")
        print()

    def mostraCadastro(self):
        self.logotipo()

        print("Insira os dados da série")
        print("(Campos com * são obrigatórios)")
        print()

        nomeBr = self.solicitaValor('Digite o nome*: ', 'texto', False)
        nomeOrig = self.solicitaValor('Digite o nome original: ', 'texto', True)
        genero = self.solicitaValor('Digite o gênero*: ', 'texto', True)
        paisOrig = self.solicitaValor('Digite o país de origem: ', 'texto', True)
        anoEstreia = self.solicitaValor('Digite o ano de estreia: ', 'texto', True)
        anoFim = self.solicitaValor('Digite o ano do fim: ', 'texto', True)

        # Armazena os valores no Banco de Dados
        valores = {
            "nomeBr" : nomeBr,
            "nomeOrig" : nomeOrig,
            "genero" : genero,
            "paisOrig" : paisOrig,
            "anoEstreia" : anoEstreia,
            "anoFim" : anoFim}
        self.banco.inserir('series', valores)

    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        # Verifica se está vazio
        if valor == "" and not permiteNulo:
                print("Valor inválido")
                return self.solicitaValor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
                return valor
        
        # Verifica se está no tipo correto
        if tipo == 'numero':
                try:
                        valor = float(valor)
                except ValueError:
                        print("Valor inválido")
                        return self.solicitaValor(legenda, tipo, permiteNulo)

        return valor
    
    def mostraLista (self):
            self.logotipo()
            print("Veja abaixo a lista de séries cadastradas")
            print()

            series = self.banco.buscaDados('series')

            for serie in series:
                    id, nomeBr, nomeOrig, genero, paisOrig, anoEstreia, anoFim = serie
                    print(f"Série {id} - {nomeBr} | {genero}")
            
            print()
            input("Tecle Enter para voltar ao Menu principal")
            self.limpaTela()
            self.mostraMenu()