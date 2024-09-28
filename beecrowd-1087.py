# Entrada
# A entrada contém vários casos de teste. A primeira e única linha de cada caso de teste contém quatro inteiros X1, Y1, X2 e Y2 (1 ≤ X1, Y1, X2, Y2 ≤ 8). A dama começa na casa de coordenadas (X1, Y1), e a casa de destino é a casa de coordenadas(X2, Y2). No tabuleiro, as colunas são numeradas da esquerda para a direita de 1 a 8 e as linhas de cima para baixo também de 1 a 8. As coordenadas de uma casa na linha X e coluna Y são (X, Y ).

# O final da entrada é indicado por uma linha contendo quatro zeros.

# Saída
# Para cada caso de teste da entrada seu programa deve imprimir uma única linha na saída, contendo um número inteiro, indicando o menor número de movimentos necessários para a dama chegar em sua casa de destino.



def menor_quantidade_de_movimentos_da_dama(x1, y1, x2, y2) -> int:
    movimentos = 0

    if x1 != x2:
        movimentos += 1

    if y1 != y2:
        movimentos += 1

    return movimentos


while True:
    entrada = input().split()

    if (entrada == ['0', '0', '0', '0']):
        break

    x1, y1, x2, y2 = map(int, entrada)

    print(x1, y1, x2, y2)

    print(menor_quantidade_de_movimentos_da_dama(x1, y1, x2, y2))


def menor_quantidade_de_movimentos_da_dama(x1, y1, x2, y2) -> int:
    movimentos = 0

    if x1 != x2:
        movimentos += 1

    if y1 != y2:
        movimentos += 1

    return movimentos
