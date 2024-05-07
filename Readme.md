Olá, criei uma APIRestful bem simples utilizando Flask, SQLite e JWT, com o intuito de demonstrar conhecimento, é possivel fazer as requisiçoes de registro, login e acesso a secure para testar se o JWT está funcionando corretamente.

Segue as instruções para usar está API Rest.

1 - Verifique se o Python está instalado na sua maquina com o comando python --version, se não estiver instalado, por favor instale primeiro e retorne aqui (segue o link para download https://www.python.org/downloads/)

2- Instala as dependecias que iram ser usadas. 
    - Flask 
    - flask_sqlalchemy 
    - flask_restful
    - flask_jwt_extended

3 - Agora, leia atentamente todos os comentarios para sanar suas duvidas, entenda que se trata de uma API basica que pode ser melhorada ao seu favor e entenda que você deve organizar melhor o arquivo se for usar, a informações estão todas em um unico arquivo.

4 - Rode no terminal o comando python3 app.py para iniciar o projeto

5 - Testes com POSTMAN <br>
http://localhost:5000/register

Utilizando essa rota você iri registrar o usuario, deve retornar uma mensagem no seu postman
Retornará essa mensagem segue iamgem abaixo

![Imagem Ilustrativa](https://ibb.co/q9ZLRch)


http://localhost:5000/login

Agora para a rota de login você ira usar o nome e senha cadastrado para pegar a sua chave de acesso
Retornará essa mensagem segue iamgem abaixo

![Imagem Ilustrativa](https://ibb.co/vJjfzQZ)


http://localhost:5000/secure

E por ultimo você faz a requisição para o JWT confirmar que está funcionando e que está seguro para conexão 
Retornará essa mensagem segue iamgem abaixo

![Imagem Ilustrativa](https://ibb.co/6vYZmf2)

Conclusão e informações extras: 
 <br>
    Este código pode ser usado para criar uma API RESTful com autenticação JWT. Ele pode ser reutilizado em qualquer projeto que precise de uma API com essas características. Você só precisaria modificar o modelo de banco de dados e os recursos da API para se adequar às necessidades do seu projeto. Por exemplo, você poderia adicionar mais campos ao modelo User ou adicionar mais recursos à API. Além disso, você poderia substituir o banco de dados SQLite por um banco de dados mais robusto para produção, como PostgreSQL ou MySQL.
Att Alan Feitosa!