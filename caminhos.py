from pathlib import Path

caminho = Path.home()
print(caminho)
for arquivo in caminho.glob("*"):
    caminho_arquivo = print(arquivo)