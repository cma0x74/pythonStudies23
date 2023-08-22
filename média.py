# calcula média aritmética entre dois valores
n1 = eval(input('digita um valor '))
n2 = eval(input('digita mais um valor '))
valores = [n1, n2]
print(f'a média aritmética entre os dois valores fornecidos é {sum(valores) / len(valores)}')

# len() retorna o número de itens em um objeto, e pode ser usada para obter o comprimento de vários tipos de objetos, como strings, listas, conjuntos, dicionários, entre outros

# sum() calcula a soma dos números na lista "valores", essa soma foi dividida pelo resultado da função len()