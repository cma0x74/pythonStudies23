# script que lê a velocidade de um corpo e aplica BRL R$7.00 de multa para cada km/h acima do permitido (80km/h)

v = int(input('forneça a velocidade em km/h '))

if v > int(80):
    print(f'você foi multado em BRL R${(v - 80) * 7} por excesso de velocidade')

else: 
    print(f'dessa vez você escapou, mas não pense que irá escapar sempre muahahahahaha')