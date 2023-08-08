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
    data = request.get_json()
    nome = data["nome"]
    idade = data["idade"]
    cliente.atualizar_cliente(id, nome, idade)
    return jsonify({"Mensagem": "Cliente atualizado com Sucesso!"})

# Deletando Registros
@app.route("/cliente/<int:id>", methods=["DELETE"])
def excluir_cliente(id):
    cliente.deletar_cliente(id)
    return jsonify({"Mensagem": "Cliente deletado com Sucesso!"})

# Consultando Registros
@app.route("/cliente", methods=["GET"])
def listar_clientes():
    try:
        clientes = cliente.consultar_cliente()
        return jsonify(clientes)
    except Exception as error:
        return jsonify({"erro": str(error)})


print("Servidor Iniciado")
if __name__ == "__main__":
    app.run(port=8080, host="localhost", debug=True)
