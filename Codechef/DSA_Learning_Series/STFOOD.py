import math
T = int(input())

for testcase in range(T):
    N = int(input())
    S = []
    P = []
    V = []
    max_revenue = 0
    for i in range(N):
        si, pi, vi = map(int, input().split())
        S.append(si)
        P.append(pi)
        V.append(vi)
        revenue = math.floor(pi/(si+1))*vi
        if revenue > max_revenue:
            max_revenue = revenue
    print(max_revenue)

