import sqlite3

class Database:

    def __init__(self, banco_dados):
        self.conectarBanco(banco_dados)

    def conectarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()

        self.criarTabelaSeries()

    def criarTabelaSeries(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS series(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomeBr TEXT NOT NULL,
                nomeOrig TEXT NULL,
                genero TEXT NOT NULL,
                paisOrig TEXT NULL,
                anoEstreia DATE NULL,
                anoFim DATE NULL
            )
        """)

    def inserir(self, tabela, valores):
        colunas = ', '.join(valores.keys())

        placeholders = ', '.join(['?'] * len(valores))

        # Cria a sql do banco de dados
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"

        # Executa a sql no banco de dados
        self.cursor.execute(sql, tuple(valores.values()))

        # Confirma as alterações do banco
        self.banco.commit()

        # Verifica se deu certo o armazenamento
        if self.cursor.lastrowid:
            print("Salvo com sucesso!")
            return True
        else:
            print("Erro ao cadastrar dados")
            return False
        
    def buscaDados (self, tabela, campos = '*'):
        sql = f"SELECT {campos} FROM {tabela}"

        self.cursor.execute(sql)

        # Pega todos os dados retornados pelo banco e guarda na variável dados
        dados = self.cursor.fetchall()

        return dados