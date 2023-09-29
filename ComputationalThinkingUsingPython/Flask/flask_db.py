from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
lista = []


class Aluno(db.Model):
    __tablename__ = "aluno"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.Integer, unique=True)
    curso = db.Column(db.String)
    departamento = db.Column(db.String)

    def __repr__(self):
        return f"Aluno(nome = {self.nome}, cpf = {self.cpf}, curso = {self.curso}, departamento = {self.departamento})"


class Listar(Resource):
    def get(self):
        return str(lista)


class Main(Resource):
    def post(self, nome):
        lista.append(str(nome).title())
        return f"Usuario {nome} foi adicionado com sucesso!"

    def delete(self, nome):
        if nome in lista:
            for index in range(0, len(lista)):
                if lista[index] == nome:
                    del lista[index]
                    return "Elemento removido"
        else:
            return "Elemento não existe"


class Version(Resource):
    def get(self):
        return "0.0.1"


api.add_resource(Listar, "/")
api.add_resource(Main, "/<nome>")
api.add_resource(Version, "/version")

if __name__ == "__main__":
    app.run(port=8080)
