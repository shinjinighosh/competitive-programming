T = int(input())

notes = [100, 50, 10, 5, 2, 1]

for testcase in range(T):
    N = int(input())
    result = 0
    for denomination in notes:
        number = N // denomination
        result += number
        N = N - number * denomination
        if N <= 0:
            break
    print(result)
