T = int(input())

for testcase in range(T):
    N = int(input())
    result = 0
    while N:
        k = int(N**0.5)
        result += 1
        N -= k*k
    print(result)

