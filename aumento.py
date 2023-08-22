# calcula um aumento por porcentagem

v = eval(input('insere o valor para o aumento '))
p = eval(input('insere o percentual do aumento '))

print(f'{v} com aumento de {p}% é {v + ((p/100) * v)}')