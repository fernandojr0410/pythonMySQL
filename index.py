from flask import Flask, jsonify, request
import cliente

app = Flask(__name__)

# Inserindo Registros


@app.route("/cliente", methods=["POST"])
def cadastrar_cliente():
    data = request.get_json()
    if isinstance(data, list):
        for entry in data:
            nome = entry["nome"]
            idade = entry["idade"]
            cliente.insert_cliente(nome, idade)
        return jsonify({"mensagem": "Clientes cadastrados com Sucesso!"})
    else:
        nome = data["nome"]
        idade = data["idade"]
        cliente.insert_cliente(nome, idade)
        return jsonify({"mensagem": "Cliente cadastrado com Sucesso!"})

# Atualizando Registros


@app.route("/cliente/<int:id>", methods=["PUT"])
def atualizar_registro(id):
    try:
        data = request.get_json()
        nome = data.get("nome")
        idade = data.get("idade")

        if nome is not None:
            cliente.atualizar_nome(id, nome)
        if idade is not None:
            cliente.atualizar_idade(id, idade)

        return jsonify({"Mensagem": "Cliente atualizado com Sucesso!"})
    except Exception as error:
        return jsonify({"erro": str(error)})

# Deletando Registros


@app.route("/cliente/<int:id>", methods=["DELETE"])
def excluir_cliente(id):
    cliente.deletar_cliente(id)
    return jsonify({"Mensagem": "Cliente deletado com Sucesso!"})


# Consultando todos os Registros


@app.route("/cliente", methods=["GET"])
def listar_clientes():
    try:
        clientes = cliente.listar_todos_clientes()
        return jsonify(clientes)
    except Exception as error:
        return jsonify({"erro": str(error)})

# Consultando Registros por ID


@app.route("/cliente/<int:id>", methods=["GET"])
def listar_cliente_por_id(id):
    try:
        cliente_info = cliente.consultar_cliente_por_id(id)
        return jsonify(cliente_info)
    except Exception as error:
        return jsonify({"erro": str(error)})


print("Servidor Iniciado")
if __name__ == "__main__":
    app.run(port=5050, host="localhost", debug=True)
