import os

chave = True
carros = ["Chevrolet Traker", "Chevrolet Onix", "Chevrolet Spin", 
          "Hyundai HB20", "Hyundai Tucson", "Fiat Uno",
          "Fiat Mobi", "Fiat Pulse"]
precos = [120, 90, 150, 85, 120, 60, 70, 130]
carros_alugados = []
precos_alugados = []

while chave:
    i = 0
    print(f"{10*"="}")
    print("Bem vindo a locadora de carros!")
    print(f"{10*"="}")
    comando = int(input("O que deseja fazer?\n" \
    "0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro\n"))
    
    if comando == 0:
        os.system("cls")
        for i in range(len(carros)):
            print(f"[{i}] {carros[i]} - R$ {precos[i]} /dia")
    elif comando == 1:
        os.system("cls")
        print("[ ALUGAR ] Dê uma olhada em nosso portfólio.\n")
        for i in range(len(carros)):
            print(f"[{i}] {carros[i]} - R$ {precos[i]} /dia")
        
        print(f"{10*"="}")
        codigo = int(input("Escolha o código do carro:\n"))
        dias = int(input("Escolha por quantos dias deseja alugar:\n"))

        print(f"Você escolheu o {carros[codigo]} por {dias} dias.\n")
        aluga = input(f"O aluguel totalizaria R$ {precos[codigo] * dias}. Deseja alugar?\n\n" \
                    "0 - SIM | 1 - NÃO\n")
        
        print(f"Parabéns! Você alugou o {carros[codigo]} por {dias} dias\n\n")

        carros_alugados.append(carros[codigo])
        precos_alugados.append(precos[codigo])
        carros.pop(codigo)
        precos.pop(codigo)
    elif comando == 2:
        print("Segue a lista de carros alugados. Qual você deseja devolver?")
        for i in range(len(carros_alugados)):
            print(f"[{i}] {carros_alugados[i]} - R$ {precos_alugados[i]} /dia")

        codigo = int(input("Escolha o código do carro que deseja devolver:\n"))
        print(f"Obrigado por devolver o carro {carros_alugados[codigo]}\n\n")

        carros.append(carros_alugados[codigo])
        precos.append(precos_alugados[codigo])
        carros_alugados.pop(codigo)
        precos_alugados.pop(codigo)

    print(f"{10*"="}")
    continua = int(input("0 - CONTINUAR | 1 - SAIR\n"))

    if continua == 1:
        os.system("cls")
        break
    else:
        os.system("cls")









