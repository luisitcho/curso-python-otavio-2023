## Como Iniciar o Servidor HTTP Local

Este projeto utiliza um servidor HTTP simples para servir o conteúdo do diretório `aula202_site/`. Para iniciar o servidor, você precisa ter o Python instalado e utilizar o interpretador do ambiente virtual. Siga os passos abaixo:

&nbsp;

**Ativar o Ambiente Virtual**:
   Certifique-se de que o ambiente virtual está ativado. Se você ainda não criou um ambiente virtual, você pode criá-lo com o comando:

   ```bash
   python -m venv venv
   ```

&nbsp;

**Detalhe do comando**

    
``venv/bin/python``: Especifica o interpretador Python dentro do ambiente virtual      venv. Isso garante que o comando use as dependências e configurações do ambiente virtual, isoladas do sistema global.

``-m http.server``: Executa o módulo embutido http.serverdo Python, que cria um servidor HTTP simples.

``-d aula202_site/``: Define o diretório raiz dos arquivos a serem servidos. Todos os arquivos disponíveis nessa pasta são acessíveis através do servidor.

``3333``: Especifique a porta na qual o servidor será iniciado. O servidor estará acessível em ``http://localhost:3333``.

&nbsp;

**Como funciona**

Execute o comando acima no terminal.

Abra o navegador e acesse: ``http://localhost:3333``. Isso exibirá os arquivos disponíveis na pasta ``aula202_site/``.

&nbsp;

**Exemplo de uso**

Este comando é útil para:

Testar sites ou aplicações estáticas durante o desenvolvimento.
Visualizar páginas HTML e outros arquivos diretamente no navegador.
Crie um ambiente de desenvolvimento local simples e rápido.

&nbsp;

**Requisitos**
Python instalado no ambiente virtual (``venv``).
O diretório ``aula202_site/``contém os arquivos a serem servidos.
