from sqlite3.dbapi2 import Error
from database.basics import create_connection


SQL_TABLE = """ CREATE TABLE IF NOT EXISTS ACOES (
                id integer PRIMARY KEY,
                status bool NOT NULL,
                symbol text NOT NULL,
                name text NOT NULL,
                date text NOT NULL,
                ativo real NOT NULL,
                preco real NOT NULL
                ); """


def create_db():
    """create the database using the sql_create_projects_table and the
    connection
    :return: Message status
    """
    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        # create projects table
        try:
            c = conn.cursor()
            c.execute(SQL_TABLE)
            print(" * " + "Table created sucessfully ")
        except Error as e:
            print(" * ERROR - " + e)
    else:
        print(" * ERROR - cannot create the database connection.")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()
