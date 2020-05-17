from math import log

T = int(input())
powers_of_5 = [1]

for testcase in range(T):
    N = int(input())
    k = int(log(N, 5))
    zeros_count = 0
    # so, there can be max k^th power of 5 in all the numbers up to N, i.e., in
    # the factorial of N
    for i in range(1,k+1):
        if len(powers_of_5) > i:
            zeros_count += N//powers_of_5[i]
        else:
            init = powers_of_5[-1]
            old_length = len(powers_of_5)
            for power in range(old_length, i+2):
                powers_of_5.append(powers_of_5[-1]*5)
            # assert len(powers_of_5) >= i
            zeros_count += N//powers_of_5[i]
    print(zeros_count)
