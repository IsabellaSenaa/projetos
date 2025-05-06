par=0
impar=0
soma_par=0
soma_impar=0
print('digite [0] para saida')
while True:
    valor=int(input('digite um numero'))
    if valor==0:
        break
    if valor%2==0:
      soma_par+=valor
      par+=1
    else:
       soma_impar+=valor
       impar+=1
media=soma_par/par
media2=soma_impar/impar
print('a media dos numero pares e', media)
print('a media dos numeros imparares e', media2)