Funcionalidade: Validação de defeitos conhecidos

Cenário: Exibir a imagem correta do produto

Dado que estou autenticado como "problem_user"
Quando acesso a lista de produtos
Então cada produto deve apresentar sua própria imagem
E a imagem deve corresponder ao produto apresentado