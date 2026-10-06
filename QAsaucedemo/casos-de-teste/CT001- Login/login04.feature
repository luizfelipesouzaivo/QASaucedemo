Funcionalidade: Autenticação de usuários

Contexto:
Dado que o usuário está na tela de login

Cenário: Login sem informar o usuário

Quando o usuário deixa o campo usuário em branco
E informa "secret_sauce" no campo senha
E seleciona "Login"
Então o sistema deve informar que o usuário é obrigatório