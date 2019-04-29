from conta import Conta

conta1 = Conta(123, "André", 100)
conta1.extrato()

conta2 = Conta(321, "Luis", 100)
conta1.extrato()

conta2.transfere(10, conta1)

conta1.extrato()
conta2.extrato()

conta2.saca(9999)
conta2.extrato()
print(conta2.codigo_banco())
print(Conta.codigo_banco())
print(Conta.codigos_bancos())
print(Conta.codigos_bancos()["BB"])

print(Conta.minimo_limite)

"""
conta2.set_saldo(50000)
print(conta2.get_saldo())
"""

"""
conta1.deposita(5000)
conta1.extrato()
conta1.saca(8000)
conta1.extrato()
"""