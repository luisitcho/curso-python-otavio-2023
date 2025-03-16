
# Python

Repositório apresentado ao curso de **Python 3 completo: PySide6, Django, Selenium, Regexp, Testes, TDD, POO, Design Patterns GoF, algoritmos e programação**, do **Luiz Otavio** . O objetivo é colocar em prática os conceitos aprendidos durante o curso, desenvolvendo aplicações robustas e modernas utilizando Python e suas diversas ferramentas, com foco em boas práticas de programação e arquiteturas sólidas.

## Extensões deste repositório

> ⚠️ Nota: Estes repositórios são complementares a este projeto principal.
* [Curso de Django](https://github.com/luisitcho/curso-django-otavio-2025) - Repositório dedicado a parte de Django.


## Gerenciando Dependências com ```pip-tools```

Este projeto utiliza ```pip-tools``` para gerenciar as dependências de forma eficiente.

1. Crie um arquivo ```requirements.in``` e liste nele os pacotes desejados (sem versões fixas). Exemplo:

   ```
    django
    requests
    pyinstaller
   ```
2. Gere o ```requirements.txt``` (com versões fixadas) executando:
   
   ```
    pip-compile requirements.in
   ```
3. Instale as dependências executando:

   ```
   pip install -r requirements.txt
   ```
### Comando único para gerar e instalar dependências

Se quiser gerar o ```requirements.txt``` e já instalar os pacotes, use:
```
pip-compile requirements.in && pip install -r requirements.txt
```
