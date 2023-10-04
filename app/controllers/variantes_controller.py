from flask import jsonify, request
from models.variantes import db, Variante

def criar_variante():
    data = request.json
    nova_variante = Variante(**data)
    db.session.add(nova_variante)
    db.session.commit()
    return jsonify({"message": "Variante criada com sucesso!"})

def listar_variantes():
    variantes = Variante.query.all()
    variantes_json = [{"id": variante.id, "cromossomo": variante.cromossomo, "posicao": variante.posicao, "base_referencia": variante.base_referencia, "base_alternativa": variante.base_alternativa} for variante in variantes]
    return jsonify(variantes_json)

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

def excluir_variante(variante_id):
    variante = Variante.query.get(variante_id)
    if not variante:
        return jsonify({"message": "Variante não encontrada"}), 404

    db.session.delete(variante)
    db.session.commit()
    return jsonify({"message": "Variante excluída com sucesso!"})
