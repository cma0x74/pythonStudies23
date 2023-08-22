# lê um nome e diz se nele há "Silva"

name = input('nome completo ')

new_name = name.title()
test = 'Silva' in new_name

if 'Silva' in new_name == True:
    print('há "Silva" no nome fornecido')

if 'Silva' in new_name == False:
    print('não há "Silva" no nome fornecido')