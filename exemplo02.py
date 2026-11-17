resposta = "S" # essa variavel precisa existir, pois o wile so roda se exister uma condição exstente.
while resposta == 'S':
    numero = int(input('Digite um número: '))

    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2

    print(f'Dobro: {dobro}')
    print(f'Triplo: {triplo}')
    print(f'Quadrado: {quadrado}')

    resposta = input('Quer continuar: [S/N]').upper()


