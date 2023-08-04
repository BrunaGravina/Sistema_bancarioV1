menu = """
Escolha a opção desejada:
[1] Depósito
[2] Saque
[3] Ver extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

opcao = 0

while True:
    
    opcao = input(menu)

    if opcao == "1":
      valor = float(input("Qual valor deseja depositar:"))
      if valor > 0:
       saldo +=valor
       extrato += f"Depósito de R$ {valor:.2f}\n"
      else:
       print("O valor precisa ser maior que zero.")

    elif opcao == "2":
     valor = float(input("Qual valor deseja sacar?"))
     excedeu_saldo = valor > saldo
     excedeu_limite = limite < valor
     execedeu_saques = LIMITE_SAQUES < numero_saques
     if excedeu_saldo:
       print("Seu saldo é insuficiente, tente novamente com um valor menor.")

     elif excedeu_limite:
       print("Sem sucesso, você excedeu seu limite de saques diários.")
  
     elif excedeu_limite:
       print("Você está tentando sacar um valor maior que o limite, tente novamente.")
      
     elif valor > 0:
      saldo -= valor
      extrato += f"Saque de R$ {valor:.2f}\n"
      numero_saques += 1
     
     else:
      print("Valor inválido, tente novamente.")  
       
    elif opcao == "3":
       print(extrato)
       print(f"Seu saldo atual é de: R$ {saldo: .2f}\n")

    elif opcao == "4":
     break

    else:
     print("Opção inválida, tente novamente.") 