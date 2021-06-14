from sqlite3.dbapi2 import Error

from database.conection import create_connection


def create_register(dados):
    """Cria um novo registro utilizando dados"""
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute(
            """ INSERT INTO ACOES(
                status, 
                symbol, 
                name, 
                date, 
                ativo, 
                preco)
                VALUES(?,?,?,?,?,?)""",
            (
                dados["status"],
                dados["symbol"],
                dados["nome"],
                dados["data"],
                dados["ativo"],
                dados["preco"],
            ),
        )
        conn.commit()
        c.close()
        return True, "Criado com sucesso"

    except Error as e:
        return False, e


def verify_register(dados):
    """Seleciona um id utilizando os campos symbol e data.
    Caso não receba um id com as especificações, manda os dados
    para o Create_register, se não utiliza os dados para atualização
    :return: Um boleano e uma msg referntes a efetividade da query
    """

    conn = create_connection()
    c = conn.cursor()

    # Valida uma Query selecionando um ID
    try:
        c.execute(
            '''SELECT id FROM ACOES 
                    WHERE symbol="{}" AND
                    date="{}"'''.format(
                dados["symbol"], dados["data"]
            )
        )
        # Valida se há informações através do tamanho da lista criada
        rows = c.fetchall()
        if len(rows) == 0:
            resposta, msg = create_register(dados)
            return resposta, msg
        else:
            resposta, msg = update_data(dados, rows[0])
            return resposta, msg
    except Error as e:
        return False, e


def update_data(dados, id):
    """Com base em um ID já selecionado, atualiza informações com
    os dados da nova requisição
    """
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute(
            """UPDATE ACOES
                    SET status = '{}',
                    symbol = '{}',
                    name = '{}',
                    ativo = '{}',
                    preco = '{}'
                    WHERE id  = {};""".format(
                dados["status"],
                dados["symbol"],
                dados["nome"],
                dados["data"],
                dados["ativo"],
                dados["preco"],
                id,
            )
        )
        conn.commit()
        c.close()
        return True, "Atualizado com sucesso"
    except Error as e:
        return False, e


# Feature não implementada
def select_max_data():
    """:return: srt data mais antiga da base"""
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute("select date from ACOES order by date asc limit 1")
        rows = c.fetchall()
        return rows[0][0]
    except IndexError:
        return None
