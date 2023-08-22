# lê um nome completo e retorna o primeiro e o último nome

name = input('forneça nome e sobrenome ')
new_name = name.strip()

print(f'first name = {new_name.split()[0]}')
print(f'last name = {new_name.split()[-1]}')