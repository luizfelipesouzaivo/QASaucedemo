# 🧪 Projeto de QA — SauceDemo

Projeto de **Quality Assurance (QA)** criado para praticar testes manuais e automação de testes web utilizando o **SauceDemo**.

O projeto reúne casos de teste, cenários em Gherkin, registros de bugs, evidências e testes automatizados utilizando **Python, Pytest e Playwright**.

> **Nível do projeto:** Portfólio / QA Júnior

---

## 🎯 Objetivo

O objetivo deste projeto é colocar em prática conhecimentos de QA durante o processo de testes de uma aplicação web.

As atividades realizadas incluem:

* Criação de casos de teste;
* Testes funcionais;
* Testes positivos e negativos;
* Escrita de cenários em Gherkin;
* Identificação e documentação de bugs;
* Registro de evidências;
* Automação dos principais fluxos;
* Utilização de Page Object Model;
* Geração de relatório de testes;
* Execução dos testes através do GitHub Actions.

---

## 🌐 Sistema testado

**Aplicação:** SauceDemo

**URL:** https://www.saucedemo.com/

O SauceDemo foi utilizado como ambiente de estudo para praticar testes em uma aplicação de e-commerce.

---

# 🛠️ Tecnologias utilizadas

| Tecnologia        | Utilização                       |
| ----------------- | -------------------------------- |
| 🐍 Python         | Linguagem utilizada na automação |
| 🧪 Pytest         | Framework de testes              |
| 🎭 Playwright     | Automação de testes web          |
| 📝 Gherkin        | Escrita dos cenários de teste    |
| 🔧 Git            | Controle de versão               |
| 🐙 GitHub         | Repositório do projeto           |
| ⚙️ GitHub Actions | Execução automática dos testes   |

---

# 🧪 Funcionalidades testadas

| Código | Funcionalidade | Cobertura                                    |
| ------ | -------------- | -------------------------------------------- |
| CT001  | 🔐 Login       | Login válido, inválido e campos obrigatórios |
| CT002  | 📦 Produtos    | Visualização, seleção e ordenação            |
| CT003  | 🛒 Carrinho    | Adição, remoção e validações                 |
| CT004  | 💳 Compra      | Checkout e finalização do pedido             |
| CT005  | 🧭 Menu        | Navegação e opções do menu                   |
| CT006  | 🚪 Logout      | Encerramento da sessão                       |

---

# 📝 Testes manuais

Os casos de teste foram organizados por funcionalidade e escritos utilizando **Gherkin**, buscando deixar os cenários claros e fáceis de entender.

Estrutura:

```text
casos-de-teste/
│
├── CT001- Login/
├── CT002- Produtos/
├── CT003- Carrinho/
├── CT004- Compra/
├── CT005- Menu/
└── CT006- Logout/
```

### Exemplo de cenário

```gherkin
Funcionalidade: Login

Cenário: Realizar login com credenciais válidas

Dado que o usuário esteja na página de login
Quando informar um usuário e senha válidos
E clicar em Login
Então o sistema deve apresentar a página de produtos
```

---

# 🐞 Bugs encontrados

Durante os testes foram identificados comportamentos inesperados na aplicação.

Atualmente o projeto possui **11 registros de bugs**.

Os bugs estão disponíveis em:

```text
bugs/
```

Cada registro contém informações como:

* Identificação do bug;
* Cenário;
* Passos para reprodução;
* Resultado esperado;
* Resultado obtido;
* Grau de prioridade;
* Evidência.

As evidências estão disponíveis em:

```text
evidencias/
```

---

# 🤖 Automação de testes

A automação foi desenvolvida utilizando:

```text
Python
   ↓
Pytest
   ↓
Playwright
```

Os testes automatizados foram separados por funcionalidade:

```text
tests/
│
├── test_login.py
├── test_produtos.py
├── test_carrinho.py
├── test_checkout.py
└── test_logout.py
```

---

# 🧩 Page Object Model

O projeto utiliza o padrão **Page Object Model (POM)** para separar as ações das páginas dos arquivos de teste.

Estrutura:

```text
pages/
│
├── login_page.py
├── inventory_page.py
├── cart_page.py
└── checkout_page.py
```

A utilização do POM ajuda a deixar os testes mais organizados e facilita a manutenção.

### Exemplo

Em vez de colocar toda a interação diretamente no teste:

```python
page.locator("#user-name").fill("standard_user")
page.locator("#password").fill("secret_sauce")
page.locator("#login-button").click()
```

A interação pode ficar dentro do Page Object:

```python
login_page.realizar_login(usuario, senha)
```

Isso deixa o teste mais fácil de ler.

---

# 🔎 Validações automatizadas

## 🔐 Login

* Login com usuário válido;
* Usuário inválido;
* Senha inválida;
* Campos obrigatórios.

## 📦 Produtos

* Exibição dos produtos;
* Ordenação por nome;
* Ordenação por preço;
* Validação dos preços.

## 🛒 Carrinho

* Adicionar produto;
* Remover produto;
* Validar produto no carrinho;
* Validar quantidade.

## 💳 Checkout

* Preenchimento dos dados;
* Avanço do checkout;
* Finalização da compra;
* Confirmação do pedido.

## 🚪 Logout

* Abrir menu;
* Realizar logout;
* Validar retorno para a tela de login.

---

# 📊 Relatórios

O projeto possui configuração para geração de relatório HTML utilizando `pytest-html`.

Para gerar o relatório:

```bash
pytest --html=reports/report.html --self-contained-html
```

O relatório será criado em:

```text
reports/report.html
```

---

# 🔄 GitHub Actions

O projeto possui uma configuração básica de **GitHub Actions** para executar os testes automaticamente.

Estrutura:

```text
.github/
└── workflows/
    └── tests.yml
```

Fluxo:

```text
Git Push
   ↓
GitHub Actions
   ↓
Instalação do Python
   ↓
Instalação das dependências
   ↓
Instalação do Playwright
   ↓
Execução do Pytest
   ↓
Resultado dos testes
```

---

# 📁 Estrutura do projeto

```text
QAsaucedemo/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── bugs/
│   ├── bug001.feature
│   ├── bug002.feature
│   ├── bug003.feature
│   ├── ...
│   └── bug011.feature
│
├── casos-de-teste/
│   ├── CT001- Login/
│   ├── CT002- Produtos/
│   ├── CT003- Carrinho/
│   ├── CT004- Compra/
│   ├── CT005- Menu/
│   └── CT006- Logout/
│
├── evidencias/
│   ├── bug001.png
│   ├── bug002.png
│   ├── bug003.png
│   ├── ...
│   └── bug011.png
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_produtos.py
│   ├── test_carrinho.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── reports/
│
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# 🚀 Como executar o projeto

## 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Depois:

```bash
cd QAsaucedemo
```

---

## 2. Criar ambiente virtual

No Windows:

```bash
python -m venv .venv
```

Ativar:

```bash
.venv\Scripts\activate
```

---

## 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

---

## 4. Instalar o navegador do Playwright

```bash
python -m playwright install chromium
```

---

## 5. Executar os testes

Para executar todos os testes:

```bash
pytest
```

Para visualizar mais detalhes:

```bash
pytest -v
```

---

# 📌 Comandos úteis

### Executar testes de Login

```bash
pytest tests/test_login.py -v
```

### Executar testes de Produtos

```bash
pytest tests/test_produtos.py -v
```

### Executar testes do Carrinho

```bash
pytest tests/test_carrinho.py -v
```

### Executar testes do Checkout

```bash
pytest tests/test_checkout.py -v
```

### Executar testes de Logout

```bash
pytest tests/test_logout.py -v
```

### Gerar relatório HTML

```bash
pytest --html=reports/report.html --self-contained-html
```

---

# 📚 O que estou praticando

## QA

* Testes funcionais;
* Testes positivos;
* Testes negativos;
* Testes exploratórios;
* Criação de casos de teste;
* Gherkin;
* Identificação de bugs;
* Bug Report;
* Evidências;
* Testes de regressão.

## Automação

* Python;
* Pytest;
* Playwright;
* Page Object Model;
* Fixtures;
* Assertions;
* Parametrização;
* Organização de testes.

## Ferramentas

* Git;
* GitHub;
* VS Code;
* GitHub Actions.

---

# 👨‍💻 Autor

**Luiz Felipe Souza Ivo**

**QA Júnior | Testes Manuais | Automação de Testes**

[LinkedIn](https://linkedin.com/in/luiz-felipe-souza-ivo) • [GitHub](https://github.com/luizfelipesouzaivo)

---

## 📌 Sobre este projeto

Este projeto faz parte do meu portfólio de estudos em **Quality Assurance**.

A proposta é demonstrar, de forma prática, minha evolução em testes de software, documentação de bugs e automação de testes.

O projeto está em constante evolução conforme novos conhecimentos são adquiridos.
