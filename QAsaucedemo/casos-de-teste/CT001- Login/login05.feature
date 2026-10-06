Funcionalidade: Autenticação de usuários

Contexto:
Dado que o usuário está na tela de login

Cenário: Login sem informar a senha

Quando o usuário informa "standard_user" no campo usuário
E deixa o campo senha em branco
E seleciona "Login"
Então o sistema deve informar que a senha é obrigatória