def fahrenheit_para_celsius(f):
    return 5*(f-32)/9
inicio=int(input('digite o valor inicial em fahrenheit:'))
fim=int(input("digite o valor final em fahrenheit:"))
print('\nfahrenheit|celsius')
print('-----------------')
if inicio<= fim:
    passo=1
else:
    passo=-1
for f in range(inicio, fim+passo,passo):
    c=fahrenheit_para_celsius(f)
    print(f'{f:.1f}F|{c:.3f}C')