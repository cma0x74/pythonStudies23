# aumento de 10% para salários acima de R$1.250.00 e aumento de 15% para salários inferiores ou iguais

sal = float(input('forneça o salário a receber aumento: R$'))

if sal > int(1250):
    print(f'seu salário com aumento de 10% é R${sal + ((10/100) * sal)}')

if sal <= int(1250):
    print(f'seu salário com aumento de 15% é R${sal + ((15/100) * sal)}')