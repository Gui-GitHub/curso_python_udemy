# PyPDF2 para manipular arquivos PDF (PdfMerger)
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

# Caminhos
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

# Criando a pasta
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# Saber quantas paginas possui um pdf
# print(len(reader.pages))

# ler cada pagina do pdf
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

# Aqui estamos extraindo o texto da primeira página do PDF
# print(page0.extract_text())

# Aqui estamos extraindo a imagem (0) da primeira página do PDF
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

# Aqui eu separo o pdf de acordo com suas páginas
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore


# Unindo os pdfs em um só novamente
files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(PASTA_NOVA / 'MERGED.pdf')  # type: ignore
merger.close()