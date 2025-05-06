valor1=float(input('digite o valor1'))
valor2=float(input('digite o valor2'))
operacao=input('digite o simbolo da operaçao, +, _, *, /')
if operacao=='+':
 print('resultado=valor1+valor2', '\n',valor1+valor2)
elif operacao=='-':
 print('resultado=valor1-valor2', '\n',valor1-valor2)
elif operacao=='*':
 print('resultado=valor1*valor2','\n', valor1*valor2)
elif operacao=='/' and valor2 !=0:
    print('resultado=valor1/valor2', '\n',valor1/valor2)
else:
    resultado='operacao invalida por ser divisao por 0'
    print('resultado', resultado)