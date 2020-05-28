T = int(input())

for testcase in range(T):
    A, B = map(int, input().split())
    matches_needed = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    num_matches_needed = 0
    result = str(A + B)
    while result:
        num_matches_needed += matches_needed[int(result[0])]
        result = result[1:]
    print(num_matches_needed)
