aluno = input("Digite o nome do aluno: ")
faltas = int(input("Digite a quantidade de faltas: "))

nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
media = (nota1 + nota2)/2
print(media)

if media >= 7 and faltas <= 3:
    print(aluno + " você foi aprovado")
else:
    print("Você foi reprovado")



