Funcionalidade: Autenticação de usuários

Contexto:
Dado que o usuário está na tela de login

Cenário: Login com usuário inválido

Quando o usuário informa um usuário inexistente
E informa "secret_sauce" no campo senha
E seleciona "Login"
Então o sistema deve apresentar uma mensagem de erro
E o acesso não deve ser realizado