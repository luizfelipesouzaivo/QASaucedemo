Funcionalidade: Autenticação de usuários

Contexto:
Dado que o usuário está na tela de login

Cenário: Login com senha inválida

Quando o usuário informa "standard_user" no campo usuário
E informa uma senha inválida
E seleciona "Login"
Então o sistema deve apresentar uma mensagem de erro
E o acesso não deve ser realizado