# diz se o nome de uma cidade começa com "Santo"

city = input('digite o nome de uma cidade ')

new_city = city.title()
dividido = new_city.split()

if dividido[0] == 'Santo':
    print('o nome da cidade fornecido começa com "Santo"')

if dividido[0] != 'Santo':
    print('o nome da cidade fornecido não começa com "Santo"')