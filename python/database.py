import sqlite3
from datetime import datetime

class BugTracker:
    def __init__(self):
        self.conn = sqlite3.connect('bugtracker.db')
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        # Criar tabela de bugs
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS bugs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            passos_reproduzir TEXT,
            prioridade TEXT,
            status TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Criar tabela de funcionalidades
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionalidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            comportamento_esperado TEXT,
            situacao_atual TEXT,
            prioridade TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        self.conn.commit()

    def adicionar_bug(self, titulo, descricao, passos_reproduzir, prioridade, status="Novo"):
        self.cursor.execute('''
        INSERT INTO bugs (titulo, descricao, passos_reproduzir, prioridade, status)
        VALUES (?, ?, ?, ?, ?)
        ''', (titulo, descricao, passos_reproduzir, prioridade, status))
        self.conn.commit()
        return self.cursor.lastrowid

    def adicionar_funcionalidade(self, titulo, comportamento_esperado, situacao_atual, prioridade):
        self.cursor.execute('''
        INSERT INTO funcionalidades (titulo, comportamento_esperado, situacao_atual, prioridade)
        VALUES (?, ?, ?, ?)
        ''', (titulo, comportamento_esperado, situacao_atual, prioridade))
        self.conn.commit()
        return self.cursor.lastrowid

    def listar_bugs(self):
        self.cursor.execute('SELECT * FROM bugs ORDER BY data_criacao DESC')
        return self.cursor.fetchall()

    def listar_funcionalidades(self):
        self.cursor.execute('SELECT * FROM funcionalidades ORDER BY data_criacao DESC')
        return self.cursor.fetchall()

    def atualizar_bug(self, id, titulo, descricao, passos_reproduzir, prioridade, status):
        self.cursor.execute('''
        UPDATE bugs
        SET titulo = ?, descricao = ?, passos_reproduzir = ?, prioridade = ?, status = ?
        WHERE id = ?
        ''', (titulo, descricao, passos_reproduzir, prioridade, status, id))
        self.conn.commit()

    def atualizar_funcionalidade(self, id, titulo, comportamento_esperado, situacao_atual, prioridade):
        self.cursor.execute('''
        UPDATE funcionalidades
        SET titulo = ?, comportamento_esperado = ?, situacao_atual = ?, prioridade = ?
        WHERE id = ?
        ''', (titulo, comportamento_esperado, situacao_atual, prioridade, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()