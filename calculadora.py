import os

while True:
    print("0 : Soma\n1 : Subtração\n2 : Multiplicação\n3 : Divisão\n4 : Exponenciação")
    chave_operacao = int(input("Escolha a operação que deseja realizar:\n"))

    operacoes = {0:"+",1:"-",2:"*",3:"/",4:"**"}

    print(f">>> {operacoes[chave_operacao]} escolhida")

    num_1 = int(input("Qual o primeiro valor?\n"))
    num_2 = int(input("Qual o segundo valor?\n"))

    conta = {0:num_1 + num_2,
            1:num_1 - num_2,
            2:num_1 * num_2, 
            3:num_1 / num_2, 
            4:num_1 ** num_2}

    resultado = f"{conta[chave_operacao]}"

    print(f"{num_1} {operacoes[chave_operacao]} {num_2} = {resultado}")
    print("====================================")
    
    chave_continua = int(input("Deseja fazer outra operação? 0-SIM 1-NÃO\n"))
    if chave_continua == 0:
        os.system("cls")
    else:
        break

