# Utiliza os módulos os.path.getsize e os.stat para obter dados dos arquivos (tamanho em bytes)
import math
import os
from itertools import count

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho em bytes para uma string legível (KB, MB, GB, etc.)"""

    # Se o tamanho for menor ou igual a 0, retorna '0B'
    if tamanho_em_bytes <= 0:
        return "0B"

    # Abreviações para cada ordem de grandeza
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    # Calcula o índice da abreviação usando logaritmo na base 1000 (ou base informada)
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    # Calcula o valor correspondente à potência da base
    potencia = base ** indice_abreviacao_tamanhos

    # Converte o tamanho para a unidade apropriada
    tamanho_final = tamanho_em_bytes / potencia

    # Seleciona a abreviação correta
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

# Caminho da pasta a ser percorrida
caminho = os.path.join(r'C:\Users', 'guilh', 'Downloads', 'teste_python')
counter = count()

# Percorre todas as pastas e arquivos a partir do caminho especificado
for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    # Lista os diretórios encontrados na pasta atual
    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    # Lista os arquivos encontrados na pasta atual
    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # Obtém informações do arquivo usando os.stat
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print('  ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))
        
        # ATENÇÃO: Não descomente a linha abaixo, pois ela apaga o arquivo!
        # os.unlink(caminho_completo_arquivo)
