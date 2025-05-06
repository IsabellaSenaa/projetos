numero = 3
soma = 0

print("Sequência de múltiplos de 3 até 21:")

while numero <= 21:
    print(numero)
    soma += numero  # Somador
    numero += 3     # Próximo múltiplo de 3

print("Soma dos números gerados:", soma)