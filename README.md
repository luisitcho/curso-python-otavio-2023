
# Python

Repositório apresentado ao curso de **Python 3 completo: PySide6, Django, Selenium, Regexp, Testes, TDD, POO, Design Patterns GoF, algoritmos e programação**, do **Luiz Otavio** . O objetivo é colocar em prática os conceitos aprendidos durante o curso, desenvolvendo aplicações robustas e modernas utilizando Python e suas diversas ferramentas, com foco em boas práticas de programação e arquiteturas sólidas.

## Extensões deste repositório

> ⚠️ Nota: Estes repositórios são complementares a este projeto principal.
* [Curso de Django](https://github.com/luisitcho/curso-django-otavio-2025) - Repositório dedicado a parte de Django.

---
---

# Resolvendo conflito de versões

Este projeto utiliza ```pip-tools``` para gerenciar as dependências de forma eficiente.

### **O que são conflitos de versão?**

Conflitos de versão ocorrem quando duas ou mais bibliotecas no seu projeto dependem de versões diferentes da mesma biblioteca. Por exemplo:

- A biblioteca `A` depende de `numpy>=1.20`.
- A biblioteca `B` depende de `numpy<1.22`.

Se você tentar instalar `A` e `B` no mesmo ambiente, o `pip` não conseguirá encontrar uma versão do `numpy` que satisfaça ambas as condições (`>=1.20` e `<1.22`), resultando em um conflito.

---

### **Por que o `pip-tools` ajuda?**

O `pip-tools` é uma ferramenta que resolve automaticamente esses conflitos. Ele analisa as dependências do seu projeto e gera um arquivo `requirements.txt` com versões compatíveis de todas as bibliotecas. Isso evita que você precise ajustar manualmente as versões no `requirements.txt`.

---

### **Passo a passo para resolver conflitos com `pip-tools`**

### **1. Instale o `pip-tools`**

Primeiro, você precisa instalar o `pip-tools`. Ele inclui dois comandos principais:

- `pip-compile`: Gera o `requirements.txt` a partir do `requirements.in`.
- `pip-sync`: Instala as dependências exatas do `requirements.txt` no seu ambiente.

```
pip install pip-tools
```

---

### **2. Crie o arquivo `requirements.in`**

O arquivo `requirements.in` deve conter apenas as bibliotecas principais que você usa diretamente no seu projeto. Não é necessário listar subdependências (o `pip-tools` cuidará disso).

Exemplo de `requirements.in`:

```
Django==4.2.16
flake8==7.0.0
pylint==3.1.0
mypy==1.3.0
pandas==2.0.0
requests==2.28.2
selenium==4.8.3
matplotlib==3.7.1
numpy
PySide6==6.8.2
ipython==8.12.0
jupyterlab
```

**Observações:**

- Inclua apenas as bibliotecas que você usa diretamente.
- Se uma biblioteca for uma dependência de outra (por exemplo, `numpy` é uma dependência do `pandas`), você não precisa listá-la no `requirements.in`.
- Se você precisar de versões específicas, inclua a versão (por exemplo, `Django==4.2.16`). Caso contrário, deixe sem versão para que o `pip-tools` escolha a versão mais recente compatível.

---

### **3. Gere o `requirements.txt`**

Use o comando `pip-compile` para gerar o `requirements.txt` a partir do `requirements.in`. O `pip-compile` resolverá automaticamente os conflitos de versão.

```
pip-compile requirements.in --output-file requirements.txt
```

**O que acontece aqui:**

- O `pip-compile` analisa as dependências do `requirements.in`.
- Ele resolve conflitos de versão e gera um `requirements.txt` com todas as bibliotecas e versões compatíveis.
- O arquivo `requirements.txt` inclui todas as subdependências necessárias.

---

### **4. Instale as dependências**

Agora, instale as dependências usando o `requirements.txt` gerado:

```
pip install -r requirements.txt
```

---

### **5. Verifique conflitos com `pip check`**

Depois de instalar as dependências, use o comando `pip check` para verificar se há conflitos restantes:

```
pip check
```

Se não houver conflitos, o comando não retornará nada. Se houver conflitos, ele listará as bibliotecas problemáticas. Nesse caso, ajuste o `requirements.in` e recompile o `requirements.txt`.

---

### **6. Atualize as dependências**

Sempre que você atualizar o `requirements.in`, recompile o `requirements.txt`:

```
pip-compile requirements.in --output-file requirements.txt
```

E instale as dependências novamente:

```
pip install -r requirements.txt
```

---

### **Exemplo prático**

### **1. Arquivo `requirements.in`**

```
Django==4.2.16
pandas==2.0.0
requests==2.28.2
```

### **2. Gerar `requirements.txt`**

```
pip-compile requirements.in --output-file requirements.txt
```

### **3. Conteúdo do `requirements.txt` gerado**

O `requirements.txt` terá algo assim:

```
#
# Este arquivo foi gerado automaticamente pelo pip-tools.
#
asgiref==3.8.1
    # via django
django==4.2.16
    # via -r requirements.in
numpy==1.24.2
    # via pandas
pandas==2.0.0
    # via -r requirements.in
python-dateutil==2.8.2
    # via pandas
pytz==2023.3
    # via django
requests==2.28.2
    # via -r requirements.in
six==1.16.0
    # via python-dateutil
```

### **4. Instalar dependências**

```
pip install -r requirements.txt
```

### **5. Verificar conflitos**

```
pip check
```

---

### **Resumo dos comandos**

1. Instale o `pip-tools`:
    
    ```
    pip install pip-tools
    ```
    
2. Crie o `requirements.in` com as bibliotecas principais.
3. Gere o `requirements.txt`:
    
    ```
    pip-compile requirements.in --output-file requirements.txt
    ```
    
4. Instale as dependências:
    
    ```
    pip install -r requirements.txt
    ```
    
5. Verifique conflitos:
    
    ```
    pip check
    ```
    
6. Atualize as dependências (quando necessário):
    
    ```
    pip-compile requirements.in --output-file requirements.txt
    pip install -r requirements.txt
    ```
    

---

### **Por que isso funciona?**

- O `pip-tools` resolve automaticamente os conflitos de versão, garantindo que todas as bibliotecas sejam compatíveis.
- O arquivo `requirements.txt` gerado é **determinístico**, ou seja, sempre que você compilar o `requirements.in`, o `requirements.txt` será o mesmo (a menos que você atualize o `requirements.in`).
- Isso torna o gerenciamento de dependências muito mais fácil e confiável.
