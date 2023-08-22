# script que lê três números e mostra qual é o maior e qual o menor

def main():
    while True:
        print('forneça três números')
        n1 = eval(input('primeiro número: '))
        n2 = eval(input('segundo número: '))
        n3 = eval(input('terceiro número: '))

        # maior
        bigger = n1
        if n2 > bigger:
            bigger = n2

        if n3 > bigger:
            bigger = n3

        # menor
        smaller = n1
        if n2 < smaller:
            smaller = n2

        if n3 < smaller:
            smaller = n3

        print(f'o menor número é {smaller} e o maior é {bigger}')

if __name__=='__main__':
    main()