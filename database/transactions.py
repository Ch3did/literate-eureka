from os import name
from sqlite3.dbapi2 import Error
from database.basics import create_connection


def create_register(new_reg):
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute(''' INSERT INTO ACOES(status, symbol, name, date, ativo, preco)
            VALUES(?,?,?,?,?,?)''' , (new_reg['status'], new_reg['symbol'], new_reg['nome'], new_reg['data'], new_reg['ativo'], new_reg['preco'])
        )
        conn.commit()
        c.close()
        return True, "Criado com sucesso"
        
    except Error as e: 
        return False, e


def verify_register(dados):
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute('''SELECT id FROM ACOES WHERE symbol="{}" AND date="{}"'''.format(dados['symbol'], dados['data']))
        rows = c.fetchall()
        if len(rows) == 0:
            resposta, msg = create_register(dados)
            return resposta, msg
        else:
            resposta, msg = update_data(dados,rows[0])
            return resposta, msg
    except Error as e:
        return False, e

    
    
def update_data(dados, id):
    conn = create_connection()
    c = conn.cursor()
    try: 
        c.execute('''UPDATE ACOES
                    SET status = '{}',
                    symbol = '{}',
                    name = '{}',
                    ativo = '{}',
                    preco = '{}',
                    WHERE id  = {};'''.format(dados['status'], dados['symbol'], dados['nome'], dados['data'], dados['ativo'], dados['preco'], id)
        )
        conn.commit()
        c.close()
        return True, "Atualizado com sucesso"
    except Error as e:
        return False, e




    

def select_max_data():
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute('select date from ACOES order by date asc limit 1')
        rows = c.fetchall()
        return rows[0][0]
    except IndexError:
        return None



