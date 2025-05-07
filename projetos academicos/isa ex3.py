numero = 1
soma = 0
contador = 0

print("Sequência do dobro dos números naturais até 10:")

while numero <= 10:
    dobro = numero * 2
    print(dobro)
    soma += dobro
    contador += 1
    numero += 1

media = soma / contador

print("Soma dos números gerados:", soma)
print("Média aritmética da sequência:", media)