ct=0
soma=0
maior_que_20=0
print('digite [0] para saida')
while True:
    valor=float(input('digite um valor'))
    if valor==0:
        break
    ct=ct+1
    soma=soma+valor
    if valor>20:
        maior_que_20=maior_que_20+1
media=soma/ct
print(f'a media dos valores e igual a: {media:.2f}')
print(f'a quantidade de valores digitados e:', ct)
print('a soma do valores e:', soma)
print(f'quantidade de valores maior que 20 e:', maior_que_20)