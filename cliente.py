import mysql.connector

configuracao_banco = {
    "host": "localhost",
    "user": "root",
    "password": "Positivosim0410@",
    "database": "projetoPython"
}


def insert_cliente(nome, idade):
    connection = None
    cursor = None
    try:
        if nome is None or idade is None:
            raise ValueError("Nome e idade são obrigatórios")

        connection = mysql.connector.connect(**configuracao_banco)
        connection.autocommit = True
        cursor = connection.cursor()

        sql = "INSERT INTO Cliente (Nome, Idade) VALUES (%s, %s)"
        values = (nome, idade)
        cursor.execute(sql, values)

        print("Registro Inserido com Sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao inserir dados: {error}")
    except ValueError as error:
        print(f"Erro ao inserir dados: {error}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def atualizar_cliente(IdCliente, Nome, Idade):
    try:
        connection = mysql.connector.connect(**configuracao_banco)
        connection.autocommit = True
        cursor = connection.cursor()

        sql = "UPDATE Cliente SET Nome=%s, Idade=%s WHERE IdCliente=%s"
        values = (Nome, Idade, IdCliente)
        cursor.execute(sql, values)

        
        print("Dados atualizados com Sucesso!")
    except mysql.connector.Error as error:
        print(f"Erro ao atualizar registro: {error}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def deletar_cliente(IdCliente):
    try:
        connection = mysql.connector.connect(**configuracao_banco)
        connection.autocommit = True
        cursor = connection.cursor()

        sql = "DELETE FROM Cliente WHERE IdCliente=%s"
        values = (IdCliente),
        cursor.execute(sql, values)

        
        print("Registro Deletado com Sucesso!")
    except mysql.connector.Error as error:
        print(f"Erro ao deletar registro: {error}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        


def consultar_cliente():
    try:
        connection = mysql.connector.connect(**configuracao_banco)
        connection.autocommit = True
        cursor = connection.cursor()

        sql = "SELECT * FROM Cliente"
        cursor.execute(sql)

        clientes = []
        for cliente in cursor.fetchall():
            cliente_dict = {
                "IdCliente": cliente[0],
                "Nome": cliente[1],
                "Idade": cliente[2]
            }
            clientes.append(cliente_dict)

        return clientes
    except mysql.connector.Error as error:
        raise error
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
