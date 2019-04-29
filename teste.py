def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo da conta {} é {}".format(conta["numero"], conta["saldo"]))

conta = cria_conta(123, "André", 100, 1000)
extrato(conta)

deposita(conta, 500)
extrato(conta)

saca(conta, 100)
extrato(conta)