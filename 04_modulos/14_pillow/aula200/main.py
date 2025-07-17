# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
# pip install pillow

from pathlib import Path
from PIL import Image

# Caminhos
ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / ' new.JPG'

# Abrindo a imagem original
pil_image = Image.open(ORIGINAL)
# Desempacotanto o tamanho da imagem
width, height = pil_image.size
# Informações 
exif = pil_image.info['exif']
# Redimensionando a imagem
new_width = 640
new_height = round(height * new_width / width)

# Criando a nova imagem
new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70, # Não precisa ser 100, ficaria pesado atoa
    exif=exif,
)