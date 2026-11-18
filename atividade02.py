total = 0
contador = 0

while True:
    valores = float(input('Digite os valores gastos: '))
    total += valores
    contador += 1

    resposta = input('Quer continuar registrando os gastos: [S/N]').upper()

    if resposta != 'S':
        break   
        
print(f' Despesas registradas: {contador}')       
print(f'Total de gastos: R${total:.2f}')    

