def calcular_salario(horas_trabalhadas, valor_hora):
    return horas_trabalhadas*valor_hora
def main():
    horas=float(input('digite o numero de horas trabalhadas:'))
    valor=float(input('digite o valor da hora trabalhada:'))
    salario= calcular_salario(horas, valor)
    print('salario bruto:', salario)
main()