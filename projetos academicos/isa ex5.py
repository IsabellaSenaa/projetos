valor_inicial = int(input("Digite o valor inicial da sequência: "))
numero = valor_inicial
contador = 0

print("Sequência de números naturais decrescentes até 0:")

while numero >= 0:
    print(numero)
    contador += 1
    numero -= 1

print("Quantidade de números gerados:", contador)