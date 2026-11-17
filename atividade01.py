meta = 2000
resultado = ''
continuar = 's'


while continuar == "s":
    venda = float(input('Qual o valor da venda ?'))
    atingimento = venda / meta *100
    resultado = resultado + f'Vendido: R$ {venda:.2f} | Atingimento: {atingimento:.1f}%\n'
    continuar = input('Cadastrar outra venda? (s/n): ').lower()

print()
print(resultado)
    
