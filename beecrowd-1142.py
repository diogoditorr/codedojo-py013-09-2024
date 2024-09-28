linhas = int(input())

for linha in range(linhas):
    sequencia = range(1 + (linha * 4), (linha + 1) * 4)

    sequencia_de_strings = [str(x) for x in sequencia]

    print(f"{' '.join(sequencia_de_strings)} PUM")