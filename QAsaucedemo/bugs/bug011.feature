Funcionalidade: Validação de defeitos conhecidos

Cenário: Realizar login dentro de um tempo aceitável

Dado que estou na tela de login
Quando informo o usuário "performance_glitch_user"
E informo a senha "secret_sauce"
E seleciono "Login"
Então o sistema deve concluir o login
E a página de produtos deve ser carregada dentro do tempo esperado