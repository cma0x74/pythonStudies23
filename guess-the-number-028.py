# escolhe um número inteiro entre 1 e 50 e deixa o user advinhar

from random import randint

number = randint(1, 50)
tentativas = 0

while True:
    try:
        palpite = int(input('digite um número inteiro entre 1 e 50: '))
        tentativas += 1

        if palpite > number:
            print('palpite errado, o número é menor, tente novamente')

        if palpite < number:
            print('palpite errado, o número é maior, tente novamente')

        if palpite == number:
            print('PARABÉNS!!! você acertou o número')
            break

    except ValueError:
        print('digite um número válido')