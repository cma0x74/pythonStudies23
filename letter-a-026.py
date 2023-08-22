# lê uma frase e retorna quantas vezes aparece a letra "a", em que posição aparece pela primeira vez e em que posição aparece pela última vez

f = input('digite algo ')

new_f = f.lower()

print(f'há {new_f.count("a")} "a"')
print(f'o primeiro "a" aparece na posição {new_f.find("a")}')
print(f'o último "a" aparece na posição {new_f.rfind("a")}')