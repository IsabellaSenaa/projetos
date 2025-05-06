genero=input("digite 'M' para masculino ou 'F' para feminino")
altura=float(input('digite sua altura em metros'))
if genero=='M':
    peso=(72.7*altura)-58
    print(f'seu peso ideal é {peso:.2f}kg')
else:
    if genero=='F':
        peso=(62.1*altura)-44.7
        print(f'seu peso ideal é {peso:.2f}kg')
    else:
        print('entrada invalida')


