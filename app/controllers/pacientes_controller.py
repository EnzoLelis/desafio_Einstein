from flask import jsonify, request
from models.pacientes import db, Paciente

def criar_paciente():
    data = request.json
    novo_paciente = Paciente(**data)
    db.session.add(novo_paciente)
    db.session.commit()
    return jsonify({"message": "Paciente criado com sucesso!"})

def listar_pacientes():
    pacientes = Paciente.query.all()
    pacientes_json = [{"id": paciente.id, "nome_completo": paciente.nome_completo, "idade": paciente.idade, "sexo": paciente.sexo} for paciente in pacientes]
    return jsonify(pacientes_json)


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


def excluir_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return jsonify({"message": "Paciente não encontrado"}), 404

    db.session.delete(paciente)
    db.session.commit()
    return jsonify({"message": "Paciente excluído com sucesso!"})