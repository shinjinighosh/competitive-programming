T = int(input())

for testcase in range(T):
    B = int(input())
    # if n = B//2, result is sum 1...(n-1) = n*(n-1)/2
    n = B // 2
    print(int(n * (n - 1) / 2))
