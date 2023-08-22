# converte real para outras moedas ae
# USD dólar hoje (16/07/23): BRL R$4.79
# KRW won hoje: BRL R$0.0038
# JPY iene hoje: BRL R$0.035

brl = eval(input('digita um valor em reais '))
usd = (brl / 4.79)
krw = (brl / 0.0038)
jpy = (brl/ 0.035)

print(f'você possui {usd:.2f} dólares, {krw:.2f} wons e {jpy:.2f} ienes')