valor1=int(input('digite o valor1'))
valor2=int(input('digite o valor 2'))
valor3=int(input('digite o valor 3'))
if valor1>valor2 and valor1>valor3 or (not(valor2>valor1 or valor3>valor1)):
    print('o maior numero e o valor1',valor1)
elif valor2>valor1 and valor2>valor3 or (not(valor1>valor2 or valor3>valor2)):
    print('o maior numero e o valor2', valor2)
else:
    print('o maior numero e o valor3', valor3)