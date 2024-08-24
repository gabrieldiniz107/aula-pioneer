print('Média dos alunos')
# codigo que recebe 4 notas de um aluno e 

nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))
nota3 = float(input('Informe a 3° nota: '))
nota4 = float(input('Informe a 4° nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média do aluno foi: {media}')

if media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')







# faz a média aritmética das notas

# se a nota final for menor que 7:
    # mostrar a mensagem "aluno reprovado" 

# e se for maior ou igual a 7:
    #imprimir a mensagem: "aluno aprovado"