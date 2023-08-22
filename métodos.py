# tipo primitivo e métodos de testes de tipos
algo = input('digita algo ')
print('esse algo é numérico?', algo.isnumeric())
print('esse algo é alfabético?', algo.isalpha())
print('esse algo é alfanumérico?', algo.isalnum())
print('esse algo possui somente caracteres maiúsculos?', algo.isupper())
print('esse algo possui somente caracteres minúsculos?', algo.islower())
print('esse algo pode ser impresso?', algo.isprintable())
print('esse algo contém somente espaços?', algo.isspace())