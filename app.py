from flask import Flask  # Importa a classe Flask que é um objeto WSGI.
from flask_sqlalchemy import SQLAlchemy  # Importa SQLAlchemy, um ORM para interagir com bancos de dados SQL.
from flask_restful import Resource, Api, request  # Importa classes do Flask-RESTful, um pacote para construir APIs REST.
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity  # Importa classes do Flask-JWT-Extended, um pacote para lidar com autenticação JWT.

app = Flask(__name__)  # Cria uma instância da classe Flask.

app.config['SECRET_KEY'] = 'SUPER-SECRET-KEY'  # Define a chave secreta para a aplicação.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Define o URI do banco de dados.

db = SQLAlchemy(app)  # Cria uma instância do SQLAlchemy.
api = Api(app)  # Cria uma instância do Api.
jwt = JWTManager(app)  # Cria uma instância do JWTManager.

class User(db.Model):  # Define a classe User como um modelo de banco de dados.
    id = db.Column(db.Integer, primary_key=True)  # Define a coluna 'id'.
    username = db.Column(db.String(100), unique=True, nullable=False)  # Define a coluna 'username'.
    password = db.Column(db.String(100), nullable=False)  # Define a coluna 'password'.

with app.app_context():  # Cria um contexto de aplicação.
    db.create_all()  # Cria todas as tabelas definidas.

class UserRegistration(Resource):  # Define a classe UserRegistration como um recurso da API.
    def post(self):  # Define o método POST para este recurso.
        data = request.get_json()
        username = data['username']
        password = data['password']

        if not username or not password:
            return {'message' :'Está faltando nome de usuario ou senha'}, 400
        if User.query.filter_by(username= username).first():
            return {'message':"Esse nome já está em uso"}, 400
        

        new_user = User(username=username, password = password)
        db.session.add(new_user)
        db.session.commit()
        return {'message':'Usuario criado com sucesso'},200

class UserLogin(Resource):  
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username= username).first()

        if user and user.password == password:
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        
        return {'message':'Credencias invalidas'},401
    
class ProtectedResource(Resource):  # Define a classe ProtectedResource como um recurso da API.
    @jwt_required()  # Exige que um token JWT válido seja fornecido para acessar este recurso.
    def get(self):  # Define o método GET para este recurso.
        current_user_id = get_jwt_identity()
        return {'message': f"Olá usuario {current_user_id}, você acessou o recurso protegido :)"}, 200

api.add_resource(UserRegistration, '/register')  # Adiciona o recurso UserRegistration à API no endpoint '/register'.
api.add_resource(UserLogin, '/login')  # Adiciona o recurso UserLogin à API no endpoint '/login'.
api.add_resource(ProtectedResource, '/secure')  # Adiciona o recurso ProtectedResource à API no endpoint '/secure'.

if __name__ == "__main__":
    app.run(debug=True)  # Inicia a aplicação em modo de depuração.