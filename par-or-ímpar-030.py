# script que lê um numero inteiro qualquer e diz se ele é par ou ímpar

def main(): # daqui pra frente sempre que possível vou usar isso
    n = int(input('digite um número inteiro '))

    if (n % 2) == int(0):
        print(f'{n} é um número par')

    else:
        print(f'{n} é um número ímpar')

if __name__ == '__main__':
    while True:
        main()
        quest = input('recomeçar? (s/n): ')
        if quest.lower() != 's':
            break