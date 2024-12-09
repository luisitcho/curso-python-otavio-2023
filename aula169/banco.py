from contas import Conta, ContaCorrente, ContaPoupanca
from pessoas import Cliente, Pessoa


class Banco:
    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes: list[Pessoa] | None = None,
                 contas: list[Conta] | None = None
                 ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: Pessoa, conta: Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name} {attrs}'


if __name__ == '__main__':

    c1 = Cliente('Luiz', 30)
    cc1 = ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1

    c2 = Cliente('Maria', 18)
    cp1 = ContaPoupanca(112, 223, 100)
    c2.conta = cp1

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    # print(banco.autenticar(c1, cc1))
    # print(banco)

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)
