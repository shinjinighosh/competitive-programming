T = int(input())

for testcase in range(T):
    K, d0, d1 = map(int, input().split())
    digits = [d0, d1]
    cumsum = [d0, d0+d1]
    cumsum_modulo_3 = (d0 + d1)%3
    for i in range(2, K):
        # new_digit = cumsum[-1]%10
        new_digit = sum(digits)%10
        cumsum.append(new_digit)
        digits.append(new_digit)
        cumsum_modulo_3 = (cumsum_modulo_3 + new_digit)%3
    if cumsum_modulo_3:
        print("NO")
    else:
        print("YES")
