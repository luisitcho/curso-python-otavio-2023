# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def cria_funcao(func):
    def interna(*args, **kwargs):
        print('Vou decorar!')

        for arg in args:
            e_string(arg)

        resultado = func(*args, **kwargs)
        print(f'O resultado foi {resultado}')
        print('Foi decorado!')

        return resultado
    return interna


@cria_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


# inverte_string_criando_parametro = cria_funcao(inverte_string)
invertida = inverte_string('123')
print(invertida)
