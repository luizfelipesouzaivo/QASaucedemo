Funcionalidade: Navegação do menu

Contexto:
Dado que o usuário está autenticado

Cenário: Realizar logout

Dado que o menu está aberto
Quando o usuário seleciona "Logout"
Então o sistema deve encerrar a sessão
E deve direcionar para a tela de login