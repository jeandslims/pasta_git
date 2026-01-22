from pathlib import Path
import os

caminho = Path.home() / 'Documents'
print(Path(caminho).glob('*'))