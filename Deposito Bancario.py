class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.transacoes = []
        self.limite_saque = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.limite_saque > 0 and 0 < valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -R${valor:.2f}")
            self.limite_saque -= 1
            print(f"Saque de R${valor:.2f} realizado com sucesso. Restam {self.limite_saque} saques.")
        else:
            if self.limite_saque <= 0:
                print("Limite de saques atingido.")
            else:
                print("Saldo insuficiente ou valor inválido para saque.")

    def extrato(self):
        print("============== Extrato ==================")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

# Criação de uma conta bancária com saldo inicial de R$ 1000.00
conta = ContaBancaria(1000.00)

while True:
    print("\nOpções:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Digite o valor para depósito: "))
        conta.depositar(valor)
    elif opcao == 2:
        valor = float(input("Digite o valor para saque: "))
        conta.sacar(valor)
    elif opcao == 3:
        conta.extrato()
    elif opcao == 0:
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
