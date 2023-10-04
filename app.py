from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, swagger

# Inicialização do aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Definição dos modelos de dados Paciente e Variante usando SQLAlchemy
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(10), nullable=False)

class Variante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cromossomo = db.Column(db.String(10), nullable=False)
    posicao = db.Column(db.Integer, nullable=False)
    base_referencia = db.Column(db.String(10), nullable=False)
    base_alternativa = db.Column(db.String(10), nullable=False)

# Inicialização da extensão Flask-RESTPlus para criar uma API
api = Api(app, version='1.0', title='API de Cadastro de Pacientes e Variantes Genéticas',
          description='Uma API para realizar operações CRUD em pacientes e variantes genéticas')

# Definição dos namespaces para pacientes e variantes
paciente_ns = api.namespace('pacientes', description='Operações relacionadas a pacientes')
variante_ns = api.namespace('variantes', description='Operações relacionadas a variantes genéticas')

# Definição da classe de recurso para listar pacientes
@paciente_ns.route('/')
class PacienteList(Resource):
    @api.response(200, 'Lista de pacientes recuperada com sucesso.')
    def get(self):
        """Lista todos os pacientes"""
        pacientes = Paciente.query.all()
        pacientes_json = [{"id": paciente.id, "nome_completo": paciente.nome_completo, "idade": paciente.idade, "sexo": paciente.sexo} for paciente in pacientes]
        return pacientes_json, 200

# Rota para exibir a interface Swagger UI
@app.route('/swagger')
def swagger_ui():
    return render_template('swagger_ui.html', data=swagger(api))

# Definição da documentação personalizada do Swagger
@api.documentation
def custom_ui():
    return {'swagger': '2.0', 'info': api.__schema__}

# Restante do seu código, incluindo rotas CRUD para pacientes

# Rota para criar um paciente
@app.route('/pacientes', methods=['POST'])
def criar_paciente():
    data = request.json
    novo_paciente = Paciente(**data)
    db.session.add(novo_paciente)
    db.session.commit()
    return jsonify({"message": "Paciente criado com sucesso!"})

# Rota para obter todos os pacientes
@app.route('/pacientes', methods=['GET'])
def listar_pacientes():
    pacientes = Paciente.query.all()
    pacientes_json = [{"id": paciente.id, "nome_completo": paciente.nome_completo, "idade": paciente.idade, "sexo": paciente.sexo} for paciente in pacientes]
    return jsonify(pacientes_json)

# Outras rotas para atualizar, recuperar e excluir pacientes e variantes




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

# Rota para atualizar um paciente por ID
@app.route('/pacientes/<int:paciente_id>', methods=['PUT'])
def atualizar_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return jsonify({"message": "Paciente não encontrado"}), 404

    data = request.json
    paciente.nome_completo = data.get('nome_completo', paciente.nome_completo)
    paciente.idade = data.get('idade', paciente.idade)
    paciente.sexo = data.get('sexo', paciente.sexo)

    db.session.commit()
    return jsonify({"message": "Paciente atualizado com sucesso!"})

# Rota para recuperar um paciente por ID
@app.route('/pacientes/<int:paciente_id>', methods=['GET'])
def obter_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return jsonify({"message": "Paciente não encontrado"}), 404

    paciente_json = {
        "id": paciente.id,
        "nome_completo": paciente.nome_completo,
        "idade": paciente.idade,
        "sexo": paciente.sexo
    }
    return jsonify(paciente_json)

# Rota para excluir um paciente por ID
@app.route('/pacientes/<int:paciente_id>', methods=['DELETE'])
def excluir_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return jsonify({"message": "Paciente não encontrado"}), 404

    db.session.delete(paciente)
    db.session.commit()
    return jsonify({"message": "Paciente excluído com sucesso!"})

# Rota para atualizar uma variante por ID
@app.route('/variantes/<int:variante_id>', methods=['PUT'])
def atualizar_variante(variante_id):
    variante = Variante.query.get(variante_id)
    if not variante:
        return jsonify({"message": "Variante não encontrada"}), 404

    data = request.json
    variante.cromossomo = data.get('cromossomo', variante.cromossomo)
    variante.posicao = data.get('posicao', variante.posicao)
    variante.base_referencia = data.get('base_referencia', variante.base_referencia)
    variante.base_alternativa = data.get('base_alternativa', variante.base_alternativa)

    db.session.commit()
    return jsonify({"message": "Variante atualizada com sucesso!"})

# Rota para recuperar uma variante por ID
@app.route('/variantes/<int:variante_id>', methods=['GET'])
def obter_variante(variante_id):
    variante = Variante.query.get(variante_id)
    if not variante:
        return jsonify({"message": "Variante não encontrada"}), 404

    variante_json = {
        "id": variante.id,
        "cromossomo": variante.cromossomo,
        "posicao": variante.posicao,
        "base_referencia": variante.base_referencia,
        "base_alternativa": variante.base_alternativa
    }
    return jsonify(variante_json)

# Rota para excluir uma variante por ID
@app.route('/variantes/<int:variante_id>', methods=['DELETE'])
def excluir_variante(variante_id):
    variante = Variante.query.get(variante_id)
    if not variante:
        return jsonify({"message": "Variante não encontrada"}), 404

    db.session.delete(variante)
    db.session.commit()
    return jsonify({"message": "Variante excluída com sucesso!"})

