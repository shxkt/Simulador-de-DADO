import random as rd


def dice_simulator():
    dado = list(range(1, 6))
    lenght = 1

    sorteio = input('Digite SORTEIO para começar: ').upper()

    if sorteio == 'SORTEIO':
        print('Rolando os Dados')
        sort_dado = rd.sample(dado, lenght)
        print(f'Seu número sorteado foi: {sort_dado}')
    else:
        print('Era pra ter digitado sorteio :/')


dice_simulator()
