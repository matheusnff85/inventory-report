# Inventory Report

- Esse projeto funciona como um gerador de relátorios para um estoque, seguindo os padrões da Programação Orientada a Ojbetos (POO), o projeto pode receber arquivos dos tipos **JSON**, **CSV** e **XML**, a partir deles a aplicação gera dois tipos de relátorios o simples e o completo.

---

# Tecnologias utilizadas :books:

- Python, POO, Flake8.

---

# Como Utilizar a aplicação

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:matheusnff85/inventory-report.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd inventory-report`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

  Após tudo feito o programa ja pode ser executado <strong>via linha de comando</strong>.
  
  O comando a ser executado será `inventory_report`. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip:
  <code>pip install .</code>

  Agora você poderá chamar o comando `inventory_report` passando seus argumentos:
  
  <code>inventory_report `argumento1` `argumento2`</code>

  - **argumento1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

  - **argumento2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.
  
  Outra opção é invocar o comando assim:

  <code>python3 -m inventory_report.main argumento1 argumento2</code>

---

- Desenvolvido por [Matheus Marinho](https://www.linkedin.com/in/matheus-marinhodsp/).