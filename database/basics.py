import sqlite3
from sqlite3.dbapi2 import Error
from amb_var import DATABASE, SQL_TABLE

#TODO: Ajustar arquivo para fechar conexão
#TODO: Criar função para salvar e outra para verificar os dados 



def create_connection():
    """ cria uma conexão com a database SQLite
        :return: Conexão ou None
    """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as err:
        print(err)

    return conn


