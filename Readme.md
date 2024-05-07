Olá,

Criei uma API Restful simples utilizando Flask, SQLite e JWT com o objetivo de demonstrar conhecimento no desenvolvimento de APIs. Abaixo estão as instruções para usar esta API Rest:

1 - Verifique se o Python está instalado em sua máquina usando o comando python --version. Se não estiver instalado, por favor, instale primeiro.

2- Instale as dependências necessárias que serão utilizadas:
    - Flask 
    - flask_sqlalchemy 
    - flask_restful
    - flask_jwt_extended

3 - Leia atentamente todos os comentários no código para esclarecer eventuais dúvidas. Observe que a API é básica e pode ser aprimorada de acordo com suas necessidades. Considere organizar o código de forma mais estruturada, se necessário, uma vez que as informações estão todas em um único arquivo.

4 - Para iniciar o projeto, execute o seguinte comando no terminal:
    Python3 app.py

5 - Teste a API utilizando o Postman: <br>

Para registrar um usuário, faça uma requisição para: http://localhost:5000/register. Você receberá uma mensagem de confirmação.

![Imagem Ilustrativa](https://i.postimg.cc/Gp6jxrtd/Register.png)

Para fazer login, faça uma requisição para: http://localhost:5000/login, utilizando o nome de usuário e senha cadastrados para obter sua chave de acesso.

![Imagem Ilustrativa](https://i.postimg.cc/xdXRmq06/Login.png)

Para acessar uma rota segura e verificar se o JWT está funcionando corretamente, faça uma requisição para: http://localhost:5000/secure.

![Imagem Ilustrativa](https://i.postimg.cc/nz7Gd597/Secure.png)

Conclusão e Informações Extras: <br>

Este código pode ser utilizado como base para criar uma API RESTful com autenticação JWT. Ele pode ser adaptado e expandido de acordo com as necessidades do seu projeto. Por exemplo, é possível adicionar mais campos ao modelo de usuário ou incluir mais recursos na API. Além disso, para ambientes de produção, considere substituir o banco de dados SQLite por opções mais robustas, como PostgreSQL ou MySQL.

Atenciosamente,
Alan Feitosa




