# aplica desconto em porcentagem a um produto

p = eval(input('insere o preço '))
d = eval(input('insere o percentual do desconto '))

print(f'o preço com desconto de {d}% é {p - ((d / 100) * p)}')