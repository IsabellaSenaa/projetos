valor1=int(input('digite o valor1'))
valor2=int(input('digite o valor2'))
valor3=int(input('digite o valor3'))
if valor1>valor2:
    if valor1>valor3:
        print('o maior numero é o valor1', valor1)
    else:
        print('o maior numero e o valor3', valor3)
else:
    if valor2>valor3:
        print('o maior numero e o valor2', valor2)
    else:
        print('o maior numero e o valor3', valor3)