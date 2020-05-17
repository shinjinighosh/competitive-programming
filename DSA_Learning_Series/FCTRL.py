from math import log

T = int(input())

for testcase in range(T):
    N = int(input())
    k = int(log(N, 5))
    zeros_count = 0
    # so, there can be max k^th power of 5 in all the numbers up to N, i.e., in
    # the factorial of N
    for i in range(1,k+1):
        zeros_count += N//(5**i)
    print(zeros_count)
