import mysql.connector

configuracao_banco = {
    "host": "localhost",
    "user": "user",
    "password": "Positivosim@0410",
    "database": "projetoPython"
}


def insert_cliente(nome, idade):
    try:
        connection = mysql.connector.connect(configuracao_banco)
        cursor = connection.cursor()

        sql = "INSERT INTO Cliente (Nome, Idade) VALUES (%s, %s)"
        values = (nome, idade)
        cursor.execute(sql, values)

        connection.commit()
        print("Registro Inserido com Sucesso!")
    except mysql.connector.Error as error:
        print(f"Erro ao inserir dados: {error}")
    finally:
        cursor.close()
        connection.close()


def atualizar_cliente(IdCliente, Nome, Idade):
    try:
        connection = mysql.connector.connect(configuracao_banco)
        cursor = connection.cursor()

        sql = "UPDATE Cliente SET nome=%s, id=%s WHERE IdCliente=%s"
        values = (Nome, Idade, IdCliente)
        cursor.execute(sql, values)

        connection.commit()
        print("Dados atualizados com Sucesso!")
    except mysql.connector.Error as error:
        print(f"Erro ao atualizar registro: {error}")
    finally:
        cursor.close()
        connection.close()


def deletar_cliente(IdCliente):
    try:
        connection = mysql.connector.connect(configuracao_banco)
        cursor = connection.cursor()

        sql = "DELETE FROM Cliente WHERE IdCliente=%s"
        values = (IdCliente),
        cursor.execute(sql, values)

        connection.commit()
        print("Registro Deletado com Sucesso!")
    except mysql.connector.Error as error:
        print(f"Erro ao deletar registro: {error}")
    finally:
        cursor.close()
        connection.close()


def consultar_cliente():
    try:
        connection = mysql.connector.connect(configuracao_banco)
        cursor = connection.cursor()

        sql = "SELECT * FROM Cliente"
        cursor.execute(sql)

        clientes = cursor.fetchall()
        for cliente in clientes:
            print(
                f"IdCliente: {cliente[0]}, Nome: {cliente[1]}, Idade: {cliente[2]}")
    except mysql.connector.Error as error:
        print(f"Erro ao consultar cleintes: {error}")
    finally:
        cursor.close()
        connection.close()
