T = int(input())

for testcase in range(T):
    N, K = map(int, input().split())
    prices = [int(p) for p in input().split()]
    # print(N, K, prices)
    loss = 0
    for price in prices:
        if price > K:
            loss += price - K
    print(loss)

