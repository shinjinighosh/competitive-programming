T = int(input())

for testcase in range(T):
    G = int(input())
    for game in range(G):
        I, N, Q = map(int, input().split())
        if N % 2 == 0:
            # even number of coins and rounds means all odd numbered coins
            # return to original state
            # hence, equal number of heads and tails no matter start state
            print(N // 2)
        else:
            # all even numbered coins return to original state
            if I == 1:  # started with all heads
                if Q == 1:  # want to know number of heads remaining
                    print(N // 2)
                else:
                    print(N // 2 + 1)
            else:
                if Q == 2:
                    print(N // 2)
                else:
                    print(N // 2 + 1)
