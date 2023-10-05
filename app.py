from flask import Flask, request, render_template
from models.pacientes import db as pacientes_db
from models.variantes import db as variantes_db
from controllers.pacientes_controller import criar_paciente, listar_pacientes, atualizar_paciente, obter_paciente, excluir_paciente
from controllers.variantes_controller import criar_variante, listar_variantes, atualizar_variante, obter_variante, excluir_variante

# Inicialização do aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite para pacientes
app.config['SQLALCHEMY_DATABASE_URI_PACIENTES'] = 'sqlite:///database_pacientes.db'
pacientes_db.init_app(app)

# Configuração do banco de dados SQLite para variantes
app.config['SQLALCHEMY_DATABASE_URI_VARIANTES'] = 'sqlite:///database_variantes.db'
variantes_db.init_app(app)



# Inicialização da extensão Flask-RESTPlus para criar uma API
api = Api(app, version='1.0', title='API de Cadastro de Pacientes e Variantes Genéticas',
          description='Uma API para realizar operações CRUD em pacientes e variantes genéticas')

# Definição dos namespaces para pacientes e variantes
paciente_ns = api.namespace('pacientes', description='Operações relacionadas a pacientes')
variante_ns = api.namespace('variantes', description='Operações relacionadas a variantes genéticas')


# Rota para exibir a interface Swagger UI
@app.route('/swagger')
def swagger_ui():
    return render_template('swagger_ui.html', data=swagger(api))

# Definição da documentação personalizada do Swagger
@api.documentation
def custom_ui():
    return {'swagger': '2.0', 'info': api.__schema__}


# Rota para criar um paciente
@app.route('/pacientes', methods=['POST'])
def criar_paciente_route():
    return criar_paciente()

# Rota para obter todos os pacientes
@app.route('/pacientes', methods=['GET'])
def listar_pacientes_route():
    return listar_pacientes()


# Rota para atualizar um paciente por ID
@app.route('/pacientes', methods=['PUT'])
def atualizar_paciente_route():
    return atualizar_paciente()

# Rota para recuperar um paciente por ID
@app.route('/pacientes/<int:paciente_id>', methods=['GET'])
def obter_paciente_route():
        return obter_paciente()


# Rota para excluir um paciente por ID
@app.route('/pacientes/<int:paciente_id>', methods=['DELETE'])
def excluir_paciente_route():
        return excluir_paciente()


#--------------------------------#


# Rota para criar uma variante
@app.route('/variantes', methods=['POST'])
def criar_variante_route():
    return criar_variante()

# Rota para obter todas as variantes
@app.route('/variantes', methods=['GET'])
def listar_variantes_route():
    return listar_variantes()

# Rota para atualizar uma variante por ID
@app.route('/variantes/<int:variante_id>', methods=['PUT'])
def atualizar_variante_route():
        return atualizar_variante()

# Rota para recuperar uma variante por ID
@app.route('/variantes/<int:variante_id>', methods=['GET'])
def obter_variante_route():
        return obter_variante()



# Rota para excluir uma variante por ID
@app.route('/variantes/<int:variante_id>', methods=['DELETE'])
def excluir_variante_route():
        return excluir_variante()



if __name__ == '__main__':
    app.run(debug=True)