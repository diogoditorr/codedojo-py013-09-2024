A = str(input())
B = str(input())
C = str(input())

valores = {
    "0": [],
    "1": []
}

valores[A].append('A')
valores[B].append('B')
valores[C].append('C')

if len(valores["0"]) == 1:
    print(valores["0"][0])

if len(valores["0"]) == 0:
    print("*")

if len(valores["1"]) == 1:
    print(valores["1"][0])

if len(valores["1"]) == 0:
    print("*")
