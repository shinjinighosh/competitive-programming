T = int(input())

for testcase in range(T):
    S = input()
    if len(S) % 2 == 0:  # even
        left_half = S[:len(S) // 2]
        right_half = S[len(S) // 2:]
    else:
        left_half = S[:len(S) // 2]
        right_half = S[len(S) // 2 + 1:]
    if set(left_half) != set(right_half):  # not the same characters
        print("NO")
        continue
    else:
        for character in set(left_half):
            count_in_left_half = left_half.count(character)
            count_in_right_half = right_half.count(character)
            if count_in_left_half != count_in_right_half:
                print("NO")
                break
        else:
            print("YES")
