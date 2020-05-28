T = int(input())

for testcase in range(T):
    S1 = input()
    S2 = input()
    maximal_difference = 0
    minimal_difference = 0
    for i in range(len(S1)):
        if S1[i] == '?' or S2[i] == '?':
            maximal_difference += 1
        elif S1[i] != S2[i]:  # both are determined and different
            maximal_difference += 1
            minimal_difference += 1
    print(f"{minimal_difference} {maximal_difference}")
