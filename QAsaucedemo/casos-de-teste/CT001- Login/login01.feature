Funcionalidade: Autenticação de usuários

Contexto:
Dado que o usuário está na tela de login

Cenário: Login realizado com sucesso

Quando o usuário informa "standard_user" no campo usuário
E informa "secret_sauce" no campo senha
E seleciona "Login"
Então o sistema deve direcionar o usuário para a página de produtos