valor_final = int(input("Digite o valor final da sequência: "))
numero = 0
contador = 0

print("Sequência de números naturais até", valor_final, ":")

while numero <= valor_final:
    print(numero)
    contador += 1
    numero += 1

print("Quantidade de números gerados:", contador)