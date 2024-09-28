test_cases = int(input(''))
in_amount = 0
out_amount = 0

for test_case in range(test_cases):
    x = int(input())

    if 10 <= x <= 20:
        in_amount += 1
    else:
        out_amount += 1

print(f"{in_amount} in")
print(f"{out_amount} out")
    
