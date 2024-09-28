lista_ordenada = []

while True:
    m = int(input('Valor de M: '))
    n = int(input('Valor de N: '))

    if m <= 0 or n <= 0:
        lista_ordenada.sort()
        print()

        break

    lista_ordenada.append(m)
    lista_ordenada.append(n)

