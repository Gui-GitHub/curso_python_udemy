# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DOWNLOADS = os.path.join(HOME, 'Downloads')
PASTA_ORIGINAL = os.path.join(DOWNLOADS, 'teste_python')
NOVA_PASTA = os.path.join(DOWNLOADS, 'teste_python_copia')

# Apaguei a nova pasta, criei e depois exclui novamente
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# move para renomear a pasta
# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
