# script que diz se c ta em um ano bissexto or not


def main():
    while True:
        quest = int(input('quantos dias tem o mês de fevereiro no ano corrente? '))
        
        if quest == int(29):
            print('yes, o ano atual is bissexto 😎👍')

        else:
            print('o ano atual is not bissexto 😐👎')

if __name__ == '__main__':
    main()