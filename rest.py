from app import app
from controllers.pacientes_controller import criar_paciente, listar_pacientes, atualizar_paciente, obter_paciente, excluir_paciente
from controllers.variantes_controller import criar_variante, listar_variantes, atualizar_variante, obter_variante, excluir_variante

@app.route('/')
def index():
      return {
            'status':'up'
      }

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
def obter_paciente_route(paciente_id):
        return obter_paciente(paciente_id)


# Rota para excluir um paciente por ID
@app.route('/pacientes/<int:paciente_id>', methods=['DELETE'])
def excluir_paciente_route(paciente_id):
        return excluir_paciente(paciente_id)


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
def atualizar_variante_route(variante_id):
        return atualizar_variante(variante_id)

# Rota para recuperar uma variante por ID
@app.route('/variantes/<int:variante_id>', methods=['GET'])
def obter_variante_route(variante_id):
        return obter_variante(variante_id)



# Rota para excluir uma variante por ID
@app.route('/variantes/<int:variante_id>', methods=['DELETE'])
def excluir_variante_route(variante_id):
        return excluir_variante(variante_id)


if __name__ == '__main__':
    app.run(debug=True)