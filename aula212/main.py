# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpg'
MODIFIED = ROOT_FOLDER / 'modified.png'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info['exif']


# width     new_width
# height    ??

new_width = 640
new_height = round(height * new_width / width)

# print(width, height)
# print(new_width, new_height)

new_image = pil_image.resize((new_width, new_height))
new_image.save(MODIFIED, optimize=True, quality=70, exif=exif)
