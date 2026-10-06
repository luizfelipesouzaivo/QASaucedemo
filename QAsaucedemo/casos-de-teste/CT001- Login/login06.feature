Funcionalidade: Autenticação de usuários

Contexto:
Dado que o usuário está na tela de login

Cenário: Login com usuário bloqueado

Quando o usuário informa "locked_out_user" no campo usuário
E informa "secret_sauce" no campo senha
E seleciona "Login"
Então o sistema deve impedir o acesso
E deve informar que o usuário está bloqueado