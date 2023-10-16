from db import db

class Variante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cromossomo = db.Column(db.String(10), nullable=False)
    posicao = db.Column(db.Integer, nullable=False)
    base_referencia = db.Column(db.String(10), nullable=False)
    base_alternativa = db.Column(db.String(10), nullable=False)
