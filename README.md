
# Sistema Bancário em Python

Este é um programa simples de sistema bancário em Python que permite realizar operações de depósito, saque e visualização de extrato bancário.

## Funcionalidades

- **Depósito**: Você pode fazer depósitos na sua conta informando o valor desejado. O valor será adicionado ao saldo da sua conta.

- **Saque**: É possível realizar saques da sua conta desde que o valor não exceda o saldo disponível e o limite de saques (3 vezes). O valor do saque será subtraído do saldo da sua conta.

- **Extrato Bancário**: Você pode visualizar o extrato bancário, que lista todas as transações realizadas (depósitos e saques) e o saldo atual da sua conta.

## Instruções de Uso

1. Execute o programa fornecido no arquivo `Deposito Bancario.py`.
2. O programa iniciará uma interação com o usuário, mostrando um menu de opções.
3. Escolha uma das opções disponíveis digitando o número correspondente e pressionando Enter:
   - `1` para Depósito
   - `2` para Saque
   - `3` para Extrato
   - `0` para Sair
4. Siga as instruções do programa para realizar as operações desejadas.

## Limitações

- O sistema possui um limite de 3 saques por conta. Uma vez atingido esse limite, não será possível realizar mais saques.
- As operações são realizadas em uma instância de conta bancária, mas não há persistência de dados. Isso significa que os dados serão perdidos após encerrar o programa.

## Contribuições

Este é um exemplo simples de sistema bancário em Python e pode ser aprimorado e expandido de várias maneiras. Se você deseja contribuir com melhorias, correções ou novas funcionalidades, fique à vontade para fazer um fork deste repositório e enviar suas alterações por meio de um pull request.
