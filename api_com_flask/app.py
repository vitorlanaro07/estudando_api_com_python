import datetime
from json import JSONEncoder
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45))
    sexo = db.Column(db.String(45))
    pais = db.Column(db.String(150))
    data_nascimento = db.Column(db.String(15))

@app.route('/')
def home():
    return [{'Mensagem':'API com Flask'}]

@app.route('/pessoa/<int:id>', methods=["GET"])
def pessoa(id):
    pessoa = Pessoa.query.get(id)
    return jsonify(
            id=pessoa.id,
            nome=pessoa.nome,
            sexo=pessoa.sexo,
            data_de_nascimento=pessoa.data_nascimento,
            pais=pessoa.pais)


@app.route('/pessoas', methods=["GET"])
def pessoas():
    pessoas = Pessoa.query.all()
    return jsonify(pessoas)

if (__name__ == '__main__'):
    app.run(host='localhost', port=5000, debug=True)

