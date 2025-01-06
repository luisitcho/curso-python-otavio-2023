# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula195.txt'
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2025, 1, 5)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='L. H.',
    telefone='+55 (11) 7890-5432'
)


# print(json.dumps(dados, indent=4, ensure_ascii=False))
# texto = """
# Prezado(a) ${nome},
# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia ${data}. Caso deseje cancelar o serviço, entre em contato com a ${empresa} pelo telefone ${telefone}.
# Atenciosamente,
# ${empresa},
# """

# template = string.Template(texto)
# print(template.safe_substitute(dados))

class MyTemplate(string.Template):
    delimiter = '%'


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.safe_substitute(dados))
