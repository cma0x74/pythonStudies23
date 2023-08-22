# sorteia ordem de nomes em uma lista

from random import shuffle

list = ['Apolo', 'Godofredo', 'Xiranga', 'Virgulino', 'Papiro', 'Durango', 'Adomervilho']

shuffle(list)

print(f'a ordem sorteada é...')
for name in list:
    print(name)