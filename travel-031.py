# script que pede distância de uma viagem em km e calcula o preço da passagem cobrando R$0.50 por km para viagens de até 200km e cobrando R$0.45 para viagens mais longas

def main():
    while True:
        s = int(input('forneça a distância em km: '))
        if s <= int(200):
            print(f'sua viagem custará R${s * 0.5}')

        else:
            print(f'sua viagem custará R${s * 0.45}')

if __name__ == '__main__':
    main()

# quando ce cria um script que recomeça automaticamente utilizando as linhas 3 e 4 do cod acima, o script não funcionará a menos que vc utilize a condição das linhas 12 e 13