saldo = 0 
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3 

menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair 
=> """

while True: 

    opcao = input(menu) 

    if opcao == "d": 
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo = saldo + valor
            extrato = extrato + "Deposito: R$ " + str(valor) + "\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Operação falhou! O limite máximo por saque é de R$ 500.00.")
        elif numero_saque >= limite_saque:
            print("Operação falhou! Número máximo de 3 saques atingido.")
        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + "Saque: R$ " + str(valor) + "\n"
            numero_saque = numero_saque + 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print("Saldo atual: R$", saldo)

    elif opcao == "q": 
        print("Saindo do sistema")
        break

    else:
        print("Operação inválida.")
