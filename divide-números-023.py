# divide algarismos de um número entre 0 e 9999 e classifica-os

number = str(input('insira um número inteiro entre 0 e 9999 '))

caract = len(number)
if caract == 4:
    print(f'unidade = {number[3]}')
    print(f'dezena = {number[2]}')
    print(f'centena = {number[1]}')
    print(f'unid. de milhar = {number[0]}')

if caract == 3:
    print(f'unidade = {number[2]}')
    print(f'dezena = {number[1]}')
    print(f'centena = {number[0]}')

if caract == 2:
    print(f'unidade = {number[1]}')
    print(f'dezena = {number[0]}')

if caract == 1:
    print(f'unidade = {number[0]}')


# tive que fazer uma gambiarrakkkkk dps eu volto e simplifico esse cod