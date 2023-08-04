from flask import Flask, jsonify, request
import cliente

app = Flask(__name__)

# Inserindo Registros
@app.route("/cliente", methods=["POST"])
def cadastrar_cliente():
    data = request.get_json()
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
def listar_contatos():
    clientes = cliente.consultar_cliente()
    return jsonify(clientes)

print("Servidor Iniciado")
if __name__ == "__main__":
    app.run(port=8080, host="localhost", debug=True)
