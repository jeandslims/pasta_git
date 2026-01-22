import os
from pathlib import Path
caminho = Path.home()



lista_arquivos = Path.home() / "Downloads"
# print(lista_arquivos)
for arquivos in lista_arquivos.glob("*"):
    if arquivos.is_dir() and not arquivos.name.startswith("."):    
        tamanho = 0
        for arquivo in arquivos.glob("**/*"):
            if arquivo.is_file():
                tamanho += os.path.getsize(arquivo)
        print(f"- {arquivos.stem} {tamanho / 1024 / 1024 :.2f} mb")
    # for _ in range(i):
    #     if arquivos.is_dir():
    #         print(os.listdir(arquivos))
# print(os.listdir(Path.home() / "Documents"))

# print(caminho / "Downloads")
# print(os.path.getsize(caminho))