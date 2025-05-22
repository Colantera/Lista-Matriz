matriz = []

print("Digite os elementos da matriz 4x4:")
for i in range(4):
    linha = []
    for co in range(4):
        valor = int(input(f"Elemento [{i}][{co}]: "))
        linha.append(valor)
    matriz.append(linha)
print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

maior_valor = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for li in range(4):
    for co in range(4):
        if matriz[li][co] > maior_valor:
            maior_valor = matriz[li][co]
            linha_maior = li
            coluna_maior = co

print(f"\nMaior valor: {maior_valor}")
print(f"Localização: linha {linha_maior}, coluna {coluna_maior}")