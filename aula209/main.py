# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_FOLDER = ROOT_FOLDER / 'pdfs_originais'
NEW_FOLDER = ROOT_FOLDER / 'arquivos_novos'

BACEN_REPORT = ORIGINAL_FOLDER / 'R20230210.pdf'
NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(BACEN_REPORT)


# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page_zero = reader.pages[0]
image_zero = page_zero.images[0]

# print(page_zero.extract_text())
# with open(NEW_FOLDER / image_zero.name, 'wb') as image:
#     image.write(image_zero.data)

for i, page in enumerate(reader.pages, start=1):

    whiter = PdfWriter()

    with open(NEW_FOLDER / f'page_{i}.pdf', 'wb') as file:
        for page in reader.pages:
            whiter.add_page(page)
            whiter.write(file)


merger = PdfMerger()

files = [NEW_FOLDER / 'page_1.pdf', NEW_FOLDER / 'page_2.pdf']

for file in files:
    merger.append(file)

merger.write(NEW_FOLDER / 'MERGED.pdf')
merger.close()
