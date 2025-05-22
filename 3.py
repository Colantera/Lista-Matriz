alunos = []
for i in range(5):
    print(f"\nAluno {i + 1}")
    matricula = int(input("Número da matrícula: "))
    media_provas = int(input("Média das provas: "))
    media_trabalhos = int(input("Média dos trabalhos: "))
    nota_final = media_provas + media_trabalhos

    aluno = [matricula, media_provas, media_trabalhos, nota_final]
    alunos.append(aluno)

maior_nota = alunos[0][3]
matricula_maior = alunos[0][0]

for aluno in alunos:
    if aluno[3] > maior_nota:
        maior_nota = aluno[3]
        matricula_maior = aluno[0]

print(f"\nA matrícula do aluno com maior nota final é: {matricula_maior}")