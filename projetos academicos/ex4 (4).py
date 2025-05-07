valor1=10
valor2=5
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
