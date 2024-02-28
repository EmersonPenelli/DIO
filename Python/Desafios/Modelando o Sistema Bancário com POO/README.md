# Sistema Bancário com Programação Orientada a Objetos (POO)
Este é um programa em Python que simula um sistema bancário utilizando Programação Orientada a Objetos (POO). O sistema conta com classes para Cliente, Conta, Transação, Saque, Deposito, e outras, proporcionando uma estrutura mais modular e organizada.

## Estrutura do Código
* Cliente: Representa um cliente do banco, com informações como nome, data de nascimento, CPF e endereço. Pode realizar transações em suas contas.

* PessoaFisica: Subclasse de Cliente, que contém informações específicas para pessoas físicas.

* Conta: Classe base para contas bancárias, com métodos para sacar, depositar e outras operações.

* ContaCorrente: Subclasse de Conta, que inclui lógica específica para contas correntes, como limite de saque e limite total.

* Historico: Registra as transações realizadas em uma conta.

* Transacao: Classe abstrata que define a estrutura básica para transações.

* Saque e Deposito: Subclasses de Transacao, responsáveis por realizar saques e depósitos, respectivamente.

* Menu: Função que exibe um menu para interação com o usuário.

- Funções auxiliares: Diversas funções auxiliares para realizar operações como depositar, sacar, exibir extrato, criar clientes, contas, listar contas, entre outras.

## Como Usar
* Execute o programa em um ambiente Python.
* Escolha a opção desejada conforme o menu apresentado.
* Siga as instruções para cada operação.
