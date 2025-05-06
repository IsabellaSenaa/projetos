aprovados=0
reprovados=0
fez_prova=0
print('digite[-1] para saida')
while True:
    nota=float(input('digite a nota do aluno'))
    if nota==-1:
        break
    fez_prova=fez_prova+1
    if nota>=5:
        aprovados=aprovados+1
    else:
        reprovados=reprovados+1
print(f'a quantidade de alunos que fizeram a prova:', fez_prova)
print(f'a quantidade de alunos aprovados:', aprovados)
print(f'a quantidade de alunos reprovados:', reprovados)