a=float(input('digite o valor do lado 1'))
b=float(input('digite o valor do lado2'))
c=float(input('digite o valor do lado3'))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print('equilatero')
    elif a==b or b==c or a==c:
        print('isoceles')
    else:
        print('escaleno')
else:
    resultado=('nao e um triangulo')
    print(resultado)