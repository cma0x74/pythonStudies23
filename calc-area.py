# calcula área e quantidade de tinta necessária para tal pintar

# 1L de tinta - 2m²

a = eval(input('fornece um valor em metros '))
b = eval(input('fornece mais um valor em metros '))

area = (a * b)
tinta = (area / 2)

print(f'são necessários {tinta}L de tinta para pintar a área de {area}m²')