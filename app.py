from flask import Flask
from models.pacientes import db as pacientes_db
from models.variantes import db as variantes_db

# Inicialização do aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite para pacientes
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///127.0.0.1:3306'

pacientes_db.init_app(app)





