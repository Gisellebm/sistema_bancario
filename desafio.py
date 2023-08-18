# Desafio de Projeto: Criando um Sistema bancário

menu = '''

=========== MENU  ===========

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

=============================
'''


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = int(input("Digite a opcao desejada: "))

    if opcao == 1:
        print('\n-----Depósito-----')
        valor_deposito = float(input("Digite o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print(f"\nVocê fez um depósito no valor de R${valor_deposito:.2f}")
        else:
            print('Valor inválido!')
    elif opcao == 2:
        print('\n-----Saque-----')

        valor_saque = float(input("Digite o valor do saque: "))

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques excedido!")

        elif valor_saque > 500.00:
            print("Máximo de R$500.00 por dia!")

        elif valor_saque > saldo:
            print("Saldo insuficiente!")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"\nVocê fez um saque no valor de R${valor_saque:.2f}")

        else:
            print('Valor inválido!')

    elif opcao == 3:
        print('\n-----Extrato-----')
        if extrato == "":
            print("Sem movimentações no período!")
        else:
            print(extrato)
            print(f"Saldo do dia: R${saldo:.2f}")

    elif opcao == 4:
        break

    else:
        print('Opção inválida')

print(" Agradecemos por usar nossos serviços!")
